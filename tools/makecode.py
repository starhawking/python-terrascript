#!/usr/bin/env python3
"""Auto-generate provider specific modules.

   The list of providers is retrieved from the Terraform Registry.
 

   Changelog:
   
   2021-02-28 - Rewrote the main logic of this script to retrieve the
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
   
   
   Issues:
   ------
   
   2021-02-28 - Walking the Terraform Provider Registry API does not work as
                expected as the meta/next_url field prevents one from
                seeing all providers. According to its web site there should
                be 828 providers. At the moment the best result is achieved 
                when starting with '?offset=0&limit=100' but that way the 
                final list will only include 131 providers and not 828.
                As a partial work-around this script reads `tools/namespaces`
                and GETs `https://registry.terraform.io/v1/providers/NAMESPACE`
                to list all providers for that namespace.

"""

import logging
import os
import os.path
import shlex
import subprocess
import sys
import tempfile
import json
from keyword import iskeyword

import jinja2
import requests

DEBUG = True

REGISTRY_BASE_URL = 'https://registry.terraform.io/'

NAMESPACES_INPUT = 'namespaces'

RESULT_SUCCESS = 0
RESULT_FAILED = 1
RESULT_SKIPPED = 2


LEGACY_INIT_TEMPLATE = jinja2.Template(
    """# terrascript/{{ provider_name|replace('-', '_') }}/__init__.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)

import terrascript

class {{ provider_name|replace('-', '_') }}(terrascript.Provider):
    pass

"""
)

LEGACY_DATASOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/{{ provider_name|replace('-', '_') }}/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)

{%- if datasources %}
import terrascript
{%- endif -%}
{%- for datasource in datasources %}


class {{ datasource|replace('-', '_') }}(terrascript.Data):
    pass
{%- endfor %}

"""
)

LEGACY_RESOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/{{ provider_name|replace('-', '_') }}/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)

{%- if resources %}
import terrascript
{%- endif -%}
{%- for resource in resources %}


class {{ resource|replace('-', '_') }}(terrascript.Resource):
    pass
{%- endfor %}

"""
)


# The NO_NAMESPACE_TEMPLATE is used to create Python modules that
# permit importing a subset of modules without a namespace. The
# rendered output is meant to be saved as.
#
#    terrascript/{{ category }}/{{ provider.name }}.py  
# 
# category: One of 'provider', 'resource' or 'data'.
# provider: Dictionary as returned by the Terraform registry.
#
NO_NAMESPACE_TEMPLATE = jinja2.Template(
   """# terrascript/{{ category }}/{{ provider.name|replace('-', '_') }}.py
# For imports without namespace, e.g.
#
#   >>> import {{ category }}.{{ provider.name|replace('-', '_') }}
#
# instead of
#
#   >>> import {{ category }}.{{ provider.namespace }}.{{ provider.name|replace('-', '_') }}
# 
# This is only available for 'official' and 'partner' providers.

from {{ provider.name|replace('-', '_') }} import *
"""
)

# The PROVIDER_TEMPLATE is used to create 
#
#     terrascript/provider/{{ provider.namespace }}/{{ provider.name }}.py
#
# for example
#
#     terrascript/provider/hashicorp/aws.py
#
PROVIDER_TEMPLATE = jinja2.Template(
    """# terrascript/provider/{{ provider.namespace }}/{{ provider.name|replace('-', '_') }}.py
import terrascript

class {{ provider.name|replace('-', '_')  }}(terrascript.Provider):
    '''{{provider.description}}
    
    '''
    __description__ = "{{provider.description}}"
    __namespace__ = "{{provider.namespace}}"
    __source__ = "{{provider.source}}"
    __version__ = "{{provider.version}}"
    __published__ = "{{provider.published_at}}"
    __tier__ = "{{provider.tier}}"
    

__all__ = ["{{ provider.name|replace('-', '_') }}"]

"""
)


# The RESOURCES_TEMPLATE is used to create 
#
#     terrascript/resource/{{ provider.namespace }}/{{ provider.name }}.py
#
# for example
#
#     terrascript/resource/hashicorp/aws.py
#
# provider: Dictionary as returned by the Terraform registry.
# schema: "resource_schema" node in 'terraform providers schema -json'
#
RESOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/resource/{{ provider.namespace }}/{{ provider.name|replace('-', '_') }}.py
{%- if schema %}
import terrascript
{%- endif -%}
{%- for name,data in schema.items() %}


class {{ name|replace('-', '_') }}(terrascript.Resource):
    pass
{%- endfor %}

__all__ = [{% if schema -%}
{%- for name in schema.keys() %}
    "{{ name|replace('-', '_') }}",
{%- endfor %}
{% endif %}]

"""
)


# The DATASOURCES_TEMPLATE is used to create 
#
#     terrascript/data/{{ provider.namespace }}/{{ provider.name }}.py
#
# for example
#
#     terrascript/data/hashicorp/aws.py
#
# provider: Dictionary as returned by the Terraform registry.
# schema: "data_source_schema" node in 'terraform providers schema -json'
#
DATASOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/data/{{ provider.namespace }}/{{ provider.name|replace('-', '_') }}.py
{%- if schema %}
import terrascript
{%- endif -%}
{%- for name,data in schema.items() %}


class {{ name|replace('-', '_') }}(terrascript.Data):
    pass
{%- endfor %}


__all__ = [{% if schema -%}
{%- for name in schema.keys() %}
    "{{ name|replace('-', '_') }}",
{%- endfor %}
{% endif %}]

"""
)

INIT_TEMPLATE = jinja2.Template(
    """# terrascript/{{ package }}/__init__.py
    
# !!! Using wildcard imports from here is DEPPRECATED !!!

{%- for provider in providers %}
from .{{provider.namespace|replace('-', '_') }}.{{ provider.name|replace('-', '_') }} import *
{%- endfor %}

"""
)


# The MAIN_TF_TEMPLATE is used to create a temporary 'main.tf' file
# for running 'terraform providers schema -json' against.
#
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


# The LIST_OF_PROVIDERS_TEMPLATE is used to create PROVIDERS.md.
#
# results: List of (provider, RESULT, RESULT_TEXT) tuples.
#
LIST_OF_PROVIDERS_TEMPLATE = jinja2.Template(
    """## List of providers
    
This document lists the *Terraform* providers that are currently supported by *Terrascript*.

- [Official providers](#official-providers)
- [Partner providers](#partner-providers)
- [Community providers](#community-providers)
- [Unsupported providers](#unsupported-providers)
    
### Official providers
    
*Terrascript* currently supports the following official *Terraform* providers.

{%- for provider,result,result_text in results %}
{%- if result == 0 and provider.tier == 'official' %}
- [{{ provider.name }}](https://registry.terraform.io/providers/{{provider.namespace}}/{{provider.name}}/{{provider.version}}) ({{provider.namespace}}/{{provider.name}}/{{provider.version }})
{%- endif %}
{%- endfor %}

### Partner providers

*Terrascript* currently supports the following partner *Terraform* providers.

{%- for provider,result,result_text in results %}
{%- if result == 0 and provider.tier == 'partner' %}
- [{{ provider.name }}](https://registry.terraform.io/providers/{{provider.namespace}}/{{provider.name}}/{{provider.version}}) ({{provider.namespace}}/{{provider.name}}/{{provider.version }})
{%- endif %}
{%- endfor %}

### Community providers

*Terrascript* currently supports the following community *Terraform* providers.

{%- for provider,result,result_text in results %}
{%- if result == 0 and provider.tier == 'community' %}
- [{{ provider.name }}](https://registry.terraform.io/providers/{{provider.namespace}}/{{provider.name}}/{{provider.version}}) ({{provider.namespace}}/{{provider.name}}/{{provider.version }})
{%- endif %}
{%- endfor %}

### Unsupported providers

The following providers are not supported.

{%- for provider,result,result_text in results %}
{%- if result != 0 %}
- [{{ provider.name }}](https://registry.terraform.io/providers/{{provider.namespace}}/{{provider.name}}/{{provider.version}}) ({{provider.namespace}}/{{provider.name}}/{{provider.version }}) - {{ result_text }}
{%- endif %}
{%- endfor %}
 
"""
)


# The TESTS_TEMPLATE is used to generate tests for verifying that the
# Python modules generated by `makecode.py` work fine and the ones that
# failed cannot be imported.
#
# results: List of (provider, RESULT, RESULT_TEXT) tuples.
#
TESTS_TEMPLATE = jinja2.Template("""# tests/test_makecode
{%- for provider,result,result_text in results %}
# {{ provider.namespace }}/{{ provider.name }}
{%- if result != 0 %}
import provider.{{ provider.namespace }}/{{ provider.name }}
import resource.{{ provider.namespace }}/{{ provider.name }}
import data.{{ provider.namespace }}/{{ provider.name }}
from provider.{{ provider.namespace }}/{{ provider.name }} import *
from resource.{{ provider.namespace }}/{{ provider.name }} import *
from data.{{ provider.namespace }}/{{ provider.name }} import *
{% else %}

{%- endif %}
{%- endfor %}
""")

THIS_DIR = os.path.abspath(".")
MODULES_DIR = os.path.abspath("../terrascript")
CACHE_PATH = os.path.join(THIS_DIR, '.cache')


def http_get_json(url):
    """GET a URL and return the decoded JSON content.
        
       :param url: URL to resource.
       :returns: Python dictionary.        
       
    """
    logging.debug(f"{url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        logging.warning(str(e))
        return {}
    

def pythonise(name):
    return name.replace('-', '_')


def get_providers_for_namespace(namespace):
    """Retrieve a list of providers from the Terraform Registry for namespace.
    
       NOTE: This function is currently used to (partially) work around the 
             issues described at the beginning of this script for details.
             
       See `get_list_of_providers()` for more details.
             
    """
    
    
    
    url = REGISTRY_BASE_URL + f"/v1/providers/{namespace}?limit=100"
    
    data = http_get_json(url)
    
    return data.get('providers', [])
    

def get_list_of_providers():
    """Retrieve a list of providers from the Terraform Registry.
    
       NOTE: This function is currently not used. See the Issues
             section at the beginning of this script for details.
    
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
    
    url = REGISTRY_BASE_URL + '/v1/providers?offset=0&limit=100'
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
        
        
    if DEBUG:
        import pprint
        logging.debug(pprint.pformat(providers))
    
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
    
    
def create_namespace_path(category, provider):
    
    # Create a folder for the namespace if it does not exist.
    #
    namespace_path = os.path.join(MODULES_DIR, category, pythonise(f"{provider['namespace']}"))
    logging.debug(f"{namespace_path}")
    
    if not os.path.isdir(namespace_path):
        os.mkdir(namespace_path)
        
    with open(os.path.join(namespace_path, '__init__.py'), 'wt') as fp:
        fp.write(pythonise(f"# {provider['namespace']}"))
        
    return namespace_path


def create_python_module(path, template, **kwargs):
    logging.debug(f"{path}")
    
    with open(path, "wt") as fp:
        fp.write(template.render(**kwargs))


def create_provider(provider, schema):
    logging.debug(f"create_provider {provider['name']}")
    
    # Create a folder for the namespace if it does not exist.
    #
    namespace_path = create_namespace_path('provider', provider)
        
    # Create the provider module inside the namespace path.
    #
    path=os.path.join(namespace_path, pythonise(f"{provider['name']}.py"))
    create_python_module(path=path, 
                         template=PROVIDER_TEMPLATE, 
                         provider=provider, 
                         schema=schema)

        
    # For 'official' and 'partner' providers also create the module directly
    # under the 'provider' path to ensure backwards compatibility.
    #
    path=os.path.join(MODULES_DIR, 'provider', pythonise(f"{provider['name']}.py"))
    if provider['tier'] in ('official', 'partner'):
        create_python_module(path=path, 
                             template=NO_NAMESPACE_TEMPLATE, 
                             provider=provider, 
                             schema=schema,
                             category='provider')       


def create_resources(provider, schema):
    logging.debug(f"create_resources {provider['name']}")
    
    # Create a folder for the namespace if it does not exist.
    #
    namespace_path = create_namespace_path('resource', provider)
    
            
    # Create the resource module inside the namespace path.
    #
    path=os.path.join(namespace_path, pythonise(f"{provider['name']}.py"))
    create_python_module(path=path, 
                         template=RESOURCES_TEMPLATE, 
                         provider=provider,
                         schema=schema)

        
    # For 'official' and 'partner' providers also create the module directly
    # under the 'resource' path to ensure backwards compatibility.
    #
    path=os.path.join(MODULES_DIR, 'resource', pythonise(f"{provider['name']}.py"))
    if provider['tier'] in ('official', 'partner'):
        create_python_module(path=path, 
                             template=NO_NAMESPACE_TEMPLATE, 
                             provider=provider,
                             schema=schema,
                             category='resource')


def create_datasources(provider, schema):
    logging.debug(f"create_datasources {provider['name']}")
    
    # Create a folder for the namespace if it does not exist.
    #
    namespace_path = create_namespace_path('data', provider)
    
    # Create the data source module inside the namespace path.
    #
    path=os.path.join(namespace_path, pythonise(f"{provider['name']}.py"))
    create_python_module(path=path, 
                         template=DATASOURCES_TEMPLATE, 
                         provider=provider, 
                         schema=schema)

        
    # For 'official' and 'partner' providers also create the module directly
    # under the 'data' path to ensure backwards compatibility.
    #
    path=os.path.join(MODULES_DIR, 'resource', pythonise(f"{provider['name']}.py"))
    if provider['tier'] in ('official', 'partner'):
        create_python_module(path=path, 
                             template=NO_NAMESPACE_TEMPLATE, 
                             provider=provider,
                             schema=schema,
                             category='data')
      

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
       :returns: Tuple of (provider, RESULT, RESULT_TEXT)
       
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
    
    logging.info(provider["name"])
    
    
    # The 'terraform' provider is maintained manually as it is not
    # listed on the Terraform Registry. 
    #
    if provider['name'] == 'terraform':
        return (provider, RESULT_SUCCESS, '')
    
    
    # Skip all providers and namespaces that are Python keywords or invalid
    # Python identifiers.
    #
    if iskeyword(provider['name']):
        return (provider, RESULT_SKIPPED, f"{provider['name']} is a Python keyword") 
    if iskeyword(provider['namespace']):
        return (provider, RESULT_SKIPPED, f"{provider['namespace']} is a Python keyword")
    if not pythonise(provider['name']).isidentifier():
        return (provider, RESULT_SKIPPED, f"{provider['name']} is not a valid Python identifier") 
    if not pythonise(provider['namespace']).isidentifier():
        return (provider, RESULT_SKIPPED, f"{provider['namespace']} is not a valid Python identifier")
    
    
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
            return (provider, RESULT_FAILED, 'Failed to initialise provider')
            
            
            
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
            return (provider, RESULT_FAILED, 'Failed to process provider')
            
            
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
            return (provider, RESULT_FAILED, 'Failed to process provider schemas')
        
        
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

    return (provider, RESULT_SUCCESS, '')


def main():

    try:
        os.stat(os.path.join(THIS_DIR, sys.argv[0]))
    except FileNotFoundError:
        print("Script must be run from the tools/ folder", file=sys.stderr)
        sys.exit(1)
        
        
    # Read the file with the known namespaces.
    #
    providers = []
    with open(NAMESPACES_INPUT, 'rt') as fp:
        for namespace in fp:  
            namespace = namespace.strip()
            providers += get_providers_for_namespace(namespace)
    
    providers = sorted(providers, key = lambda p: p['name'])


    # Only process subset of providers if requested to do so 
    # on the command line.
    #
    if len(sys.argv) > 1:
        providers = [provider for provider in providers if provider["name"] in sys.argv[1:]]
    
    
    # Process each provider.
    #
    results = [process(provider) for provider in providers]
    
    
    # Filter out failed providers.
    #
    providers = [result[0] for result in results if result[1] == 0]
                        

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
            fp.write(LIST_OF_PROVIDERS_TEMPLATE.render(results=results))


if __name__ == "__main__":
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG, format="%(lineno)d %(msg)s")
    else:
        logging.basicConfig(level=logging.INFO)
    main()
