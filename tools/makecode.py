#!/usr/bin/env python3
"""Auto-generate provider specific modules.

   The script reads a list of Terraform providers from the file PROVIDERS, 
   pulls the provider's Github repository and parses the provider.go file.

   This script relies on the content of a provider's 'provider.go'
   matching the regular expression `REGEX` below.
   
   Runtime: 2:30 minutes

   Changelog:
   2021-02-xx - Rewrote the main logic of this script to retrieve the
                list of providers from the Terraform Registry instead of
                ``providers.yml`. In the process temporary files are
                now written to ``tools/workdir/makecode`` so it can
                be re-used in later runs.
                Added deprecation warnings to modules in the legacy
                layout, e.g. ``import terrascript.aws``.
                
   2020-08-21 - Added support for providers with dash in their name
                Cleaned up code to conform to pep8
                Fixed syntax error when (re)raising exception from process
                Updated templates to conform to black format better

   2020-01-03 - Renamed `PROVIDERS` to `providers.yml` to accomodate
                custom repository paths to community providers.
                Add inclusion of `data/terraform.py`.

   2019-09-07 - Added creation of new module layout and prefixed existing
                code with 'legacy_'.
                Removed option to execute script with a list of providers
                given on the command line. This wouldn't work anymore with
                the new module layout as the script must always know the
                full list of modules.

   2019-08-17 - Access to Github is now through the `git` command line tool
                instead of the `github3` Python module.
                Use Jinja2 for templating.
                Make the script process multiple providers concurrently.

   See https://github.com/mjuenema/python-terrascript/commits/develop/makecode.py
   for a list of earlier changes.

"""
#import concurrent.futures
import logging
import os
import os.path
import shlex
import subprocess
import sys
import tempfile
import json

import jinja2
import requests

DEBUG = True
#CONCURRENCY = 1


REGISTRY_BASE_URL = 'https://registry.terraform.io/'


LEGACY_INIT_TEMPLATE = jinja2.Template(
    """# terrascript/{{ provider_name }}/__init__.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)

import terrascript

class {{ provider_name }}(terrascript.Provider):
    pass

"""
)

LEGACY_DATASOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/{{ provider_name }}/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)

{%- if datasources %}
import terrascript
{%- endif -%}
{%- for datasource in datasources %}


class {{ datasource }}(terrascript.Data):
    pass
{%- endfor %}

"""
)

LEGACY_RESOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/{{ provider_name }}/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)

{%- if resources %}
import terrascript
{%- endif -%}
{%- for resource in resources %}


class {{ resource }}(terrascript.Resource):
    pass
{%- endfor %}

"""
)

PROVIDER_TEMPLATE = jinja2.Template(
    """# terrascript/provider/{{ provider.name }}.py
import terrascript


class {{ provider.name }}(terrascript.Provider):
    '''{{provider.description}}
    
    '''
    __description__ = "{{provider.description}}"
    __version__ = "{{provider.version}}"
    

__all__ = ["{{ provider.name }}"]

"""
)

RESOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/resource/{{ provider.name }}.py
{%- if schema_resources %}
import terrascript
{%- endif -%}
{%- for name,data in schema_resources.items() %}


class {{ name }}(terrascript.Resource):
    pass
{%- endfor %}

__all__ = [{% if schema_resources -%}
{%- for name in schema_resources.keys() %}
    "{{ name }}",
{%- endfor %}
{% endif %}]

"""
)

DATASOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/data/{{ provider.name }}.py
{%- if schema_datasources %}
import terrascript
{%- endif -%}
{%- for name,data in schema_datasources.items() %}


class {{ name }}(terrascript.Data):
    pass
{%- endfor %}


__all__ = [{% if schema_datasources -%}
{%- for name in schema_datasources.keys() %}
    "{{ name }}",
{%- endfor %}
{% endif %}]

"""
)

INIT_TEMPLATE = jinja2.Template(
    """# terrascript/{{ package }}/__init__.py
from .terraform import *
{%- for provider in providers %}
from .{{ provider.name }} import *
{%- endfor %}

"""
)

MAIN_TF_TEMPLATE = jinja2.Template(
    """terraform {
  required_providers {
    {{ provider.name }} = {
      source  = "{{ provider.namespace }}/{{ provider.name }}"
      version = "{{ provider.version }}"
    }
  }
}
"""
)

LIST_OF_PROVIDERS_TEMPLATE = jinja2.Template(
    """## List of providers
    
*Terrascript* currently supports the following *Terraform* providers.

{%- for provider in providers %}
- [{{ provider.name }}](https://registry.terraform.io/providers/{{provider.namespace}}/{{provider.name}}/{{provider.version}}) ({{ provider.version }})
{%- endfor %} 
"""
)

THIS_DIR = os.path.abspath(".")
MODULES_DIR = os.path.abspath("../terrascript")
CACHE_PATH = os.path.join(THIS_DIR, '.cache')


def http_get_json(url):
    """GET a URL and return the decoded JSON content.
        
       :param url: URL to resource.
       :returns: Python dictionary.        
       
    """
    
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
    

def get_list_of_providers():
    """Retrieve a list of providers from the Terraform Registry.
    
       Make repeated requests to the URL 
       ``https://registry.terraform.io/v1/providers?offset=X``
       until information about all providers listed on the 
       registry has been retrieved. 
       
       The function returns a list of dictionaries describing the
       providers. 
       
       ```
       [ {'alias': None,
          'description': 'terraform-provider-helm',
          'downloads': 10753398,
          'id': 'hashicorp/helm/2.0.2',
          'name': 'helm',
          'namespace': 'hashicorp',
          'owner': '',
          'published_at': '2021-01-18T20:49:49Z',
          'source': 'https://github.com/hashicorp/terraform-provider-helm',
          'tag': 'v2.0.2',
          'tier': 'official',
          'version': '2.0.2'},
         ...
       ]
       ```
    
    """
    
    url = REGISTRY_BASE_URL + '/v1/providers'
    providers = []
    previous_meta = None

    while True:
        # The loop is terminated when the meta field does no longer change.
        # The Terraform Registry does not explicitly indicate that all 
        
        logging.debug(url)  # DEBUG
        
        data = http_get_json(url) 
        # {'meta': 
        #   {'limit': 15, 
        #    'current_offset': 0, 
        #    'next_offset': 15, 
        #    'next_url': '/v1/providers?offset=15'}, 
        # 'providers': [...]
        
        # Terminate loop when meta field does not change.
        #
        if previous_meta == data['meta']:
            break
        previous_meta = data['meta']
                
        providers += data.get('providers', [])
        
        url = REGISTRY_BASE_URL + data['meta']['next_url']
    
    return providers
                            

def legacy_create_provider_directory(provider):
    providerdir = os.path.join(MODULES_DIR, provider)

    if not os.path.isdir(providerdir):
        os.mkdir(providerdir)

    return providerdir


def legacy_create_provider_init(provider_name, providerdir):
    with open(os.path.join(providerdir, "__init__.py"), "wt") as fp:
        fp.write(LEGACY_INIT_TEMPLATE.render(provider_name=provider_name))


def legacy_create_provider_datasources(provider_name, providerdir, datasources):
    with open(os.path.join(providerdir, "d.py"), "wt") as fp:
        fp.write(
            LEGACY_DATASOURCES_TEMPLATE.render(
                provider_name=provider_name, datasources=datasources
            )
        )

def legacy_create_provider_resources(provider_name, providerdir, resources):
    for resource in resources:
        logging.debug(f"legacy_create_provider_resources resource={resource}")

    with open(os.path.join(providerdir, "r.py"), "wt") as fp:
        fp.write(
            LEGACY_RESOURCES_TEMPLATE.render(provider_name=provider_name, 
                                             resources=resources)
        )


def legacy_process(provider, schema_resources, schema_datasources):
    legacy_providerdir = legacy_create_provider_directory(provider['name'])
    legacy_create_provider_init(provider['name'], legacy_providerdir)
    legacy_create_provider_datasources(provider['name'], legacy_providerdir, schema_datasources.keys())
    legacy_create_provider_resources(provider['name'], legacy_providerdir, schema_resources.keys())


def create_provider(provider, schema_provider):
    logging.debug(f"create_provider {provider['name']}")
    provider_path = os.path.join(MODULES_DIR, "provider", f"{provider['name']}.py")
    with open(provider_path, "wt") as fp:
        fp.write(PROVIDER_TEMPLATE.render(provider=provider, 
                                          schema_provider=schema_provider))


def get_sanitized_name(provider):
    """Get the string sanitized for use as python module

    :return:
    """
    return provider.replace("-", "_")


def create_resources(provider, schema_resources):
    logging.debug(f"create_resources {provider['name']}")
    resource_path = os.path.join(MODULES_DIR, "resource", f"{provider['name']}.py")
    with open(resource_path, "wt") as fp:
        fp.write(RESOURCES_TEMPLATE.render(provider=provider, 
                                           schema_resources=schema_resources))


def create_datasources(provider, schema_datasources):
    logging.debug(f"create_datasources {provider['name']}")
    datasource_path = os.path.join(MODULES_DIR, "data", f"{provider['name']}.py")
    with open(datasource_path, "wt") as fp:
        fp.write(
            DATASOURCES_TEMPLATE.render(provider=provider, 
                                        schema_datasources=schema_datasources)
        )



def read_cache(provider):
    with open(CACHE_PATH, 'at+') as fp:
        fp.seek(0)
        try:
            info = json.load(fp)            
        except json.decoder.JSONDecodeError:
            info = {}
        return info.get(provider['name'], {'version': None})
    
    
def write_cache(provider, data):
    with open(CACHE_PATH, 'at+') as fp:
        fp.seek(0)
        try:
            info = json.load(fp)
        except json.decoder.JSONDecodeError:
            info = {}
            
        info[provider['name']] = {'version': provider['version'], 'data': data}
        json.dump(info, fp)


def process(provider):
    """Process a provider.
    
       :param entry: Data for a provider (see below).
       
       ```
       {'alias': None,
        'description': 'terraform-provider-helm',
        'downloads': 10753398,
        'id': 'hashicorp/helm/2.0.2',
        'name': 'helm',
        'namespace': 'hashicorp',
        'owner': '',
        'published_at': '2021-01-18T20:49:49Z',
        'source': 'https://github.com/hashicorp/terraform-provider-helm',
        'tag': 'v2.0.2',
        'tier': 'official',
        'version': '2.0.2'}
       ``` 
    
    """
    
    # Do not process the 'registry.terraform.io/hashicorp/terraform' as it
    # is not listed on the Terraform Registry
    #
    if provider['name'] == 'terraform':
        return None
    
    logging.info(provider["name"])
    
    
    # Return cached data if the provider version has not changed.
    #
    cached_data = read_cache(provider)
    if cached_data['version'] == provider['version']:
        return json.loads(cached_data['data'])


    # Otherwise run 'terraform init' and 'terraform providers schema -json'
    # to retrieve information about the resources and data sources
    # of this provider.
    #
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = os.path.join(THIS_DIR, 'workdir', 'makecode')
        
        # Create a main.tf file for this provider.
        #
        main_tf_path = os.path.join(tmpdir, 'main.tf')
        with open(main_tf_path, 'wt') as fp:
            fp.write(MAIN_TF_TEMPLATE.render(provider=provider))
            
        
        # Execute 'terraform init'. 
        #
        cmd = "terraform init"
        result = subprocess.run(
            shlex.split(cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=tmpdir,
            text=True
            )
        if result.returncode != 0:
            logging.warning(result.stderr)
            
            
            
        # Execute 'terraform providers schema -json'
        #
        cmd = "terraform providers schema -json"
        result = subprocess.run(
            shlex.split(cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=tmpdir,
            text=True
        )
        if result.returncode != 0:
            logging.warning(result.stderr)
            
            
        # Read the output of 'terraform providers schema -json'
        #
        #   format_version    "0.1"
        #   provider_schemas    
        #     registry.terraform.io/hashicorp/aws    
        #       provider: {...}
        #       resource_schemas: {...}
        #       data_source_schemas: {...}            
        #
        try:
            data = json.loads(result.stdout)
        except json.decoder.JSONDecodeError:
            return None
        
        
    # Write the data to the cache.
    #
    write_cache(provider, data)
    
    provider_schemas = data['provider_schemas']
    key = list(provider_schemas.keys())[0]
    
    # Note: `provider` was passed to this function.
    schema_provider = data['provider_schemas'][key]['provider']
    schema_resources = data['provider_schemas'][key].get('resource_schemas', {})
    schema_datasources = data['provider_schemas'][key].get('data_source_schemas', {})
    

    # The legacy layout creates
    #
    # PROVIDER/__init__.py
    # PROVIDER/r/py
    # PROVIDER/d/py
    #
    legacy_process(provider, schema_resources, schema_datasources)

    # The new layout creates
    #
    # providers/PROVIDER.py
    # resources/PROVIDER.py
    # datasources/PROVIDER.py
    #
    create_provider(provider, schema_provider)
    create_resources(provider, schema_resources)
    create_datasources(provider, schema_datasources)

    return provider

def main():

    try:
        os.stat(os.path.join(THIS_DIR, sys.argv[0]))
    except FileNotFoundError:
        print("Script must be run from the tools/ folder", file=sys.stderr)
        sys.exit(1)
        
    providers = sorted(get_list_of_providers(), key = lambda p: p['name'])


    # Only process subset of providers if requested to do so 
    # on the command line.
    #
    if len(sys.argv) > 1:
        providers = [provider for provider in providers if provider["name"] in sys.argv[1:]]
    
    
    # Process each provider. The returned value will be ``None`` if 
    # processing a provider failed so it can be filtered later.
    #
    results = [process(provider) for provider in providers]
                        

    # Create the __ini__.py files for providers, datasources and resources.
    #
    with open(os.path.join(MODULES_DIR, "provider", "__init__.py"), "wt") as fp:
        fp.write(INIT_TEMPLATE.render(providers=providers, package="provider"))

    with open(os.path.join(MODULES_DIR, "resource", "__init__.py"), "wt") as fp:
        fp.write(INIT_TEMPLATE.render(providers=providers, package="resource"))

    with open(os.path.join(MODULES_DIR, "data", "__init__.py"), "wt") as fp:
        fp.write(INIT_TEMPLATE.render(providers=providers, package="data"))
        
    
    # Write the sorted list of providers into ../PROVIDERS.md but only
    # if all providers were processed. 
    #
    if len(sys.argv) == 1:
        with open(os.path.join('..','PROVIDERS.md'), 'wt') as fp:
            fp.write(LIST_OF_PROVIDERS_TEMPLATE.render(providers=providers))


if __name__ == "__main__":
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG, format="%(lineno)d %(msg)s")
    else:
        logging.basicConfig(level=logging.INFO)
    main()
