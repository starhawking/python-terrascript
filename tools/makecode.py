#!/usr/bin/env python3

"""Auto-generate terrascript/PROVIDER/{r,d}.py files.

   If called without any argument(s), the script reads a list of Terraform
   providers from the file PROVIDERS, pulls the provider's Github
   repository and parses the provider.go file.

   Alternatively this script can be called with the name of one or more
   providers as argument(s) instead of reading the file PROVIDERS. This
   is useful if a provider is either not (yet) listed in PROVIDERS or
   only a subset of providers is to be updated.

   This script relies on the content of a provider's 'provider.go'
   matching the regular expression `REGEX` below. Providers for which this
   is not the case can be added manually.

   Changelog:

   2019-08-17 - Access to Github is now through the `git` command line tool
                instead of the `github3` Python module.
                Use Jinja2 for templating.
                Make the script process multiple providers concurrently.

   See https://github.com/mjuenema/python-terrascript/commits/develop/makecode.py
   for a list of earlier changes.

"""

DEBUG = True
CONCURRENCY = 10

import os
import os.path
import sys
import re
import tempfile
import subprocess
import shlex
import concurrent.futures
import jinja2
import logging


if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)


#REGEX = re.compile(b'".*?_(?P<name>.+)":\s+(?P<type>resource|data)')
REGEX = re.compile(b'"(?P<name>.+)":\s+(?P<type>resource|data)')
"""REGEX to extract the names of resources and data sources from a provider.go file.

    DataSourcesMap: map[string]*schema.Resource{
            "alicloud_account":                dataSourceAlicloudAccount(),
            "alicloud_images":                 dataSourceAlicloudImages(),
            "alicloud_regions":                dataSourceAlicloudRegions(),
            ...
             ^^^^^^^^^^^^^^^^                  ^^^^

    ResourcesMap: map[string]*schema.Resource{
            "alicloud_instance":               resourceAliyunInstance(),
            "alicloud_ram_role_attachment":    resourceAlicloudRamRoleAttachment(),
            "alicloud_disk":                   resourceAliyunDisk(),
            ...
             ^^^^^^^^^^^^^^^^                  ^^^^^^^^

   This only works reliably if the provider.go file follows exactly this
   naming convention but its still much better than having to add all
   resources and data source manually.

"""

INIT_TEMPLATE = jinja2.Template("""# terrascript/{{ provider }}/__init__.py

import terrascript

class {{ provider }}(terrascript.Provider):
    pass
""")

DATASOURCES_TEMPLATE = jinja2.Template("""#  terrascript/{{ provider }}/d.py

import terrascript

{% for datasource in datasources %}
class {{ datasource }}(terrascript.Data):
    pass
{% endfor %}
""")

RESOURCES_TEMPLATE = jinja2.Template("""#  terrascript/{{ provider }}/r.py

import terrascript

{% for resource in resources %}
class {{ resource }}(terrascript.Resource):
    pass
{% endfor %}
""")



def create_provider_directory(provider, modulesdir):

    providerdir = os.path.join(modulesdir, provider)

    if not os.path.isdir(providerdir):
        os.mkdir(providerdir)

    return providerdir


def create_provider_init(provider, providerdir):

    with open(os.path.join(providerdir, '__init__.py'), 'wt') as fp:
        fp.write(INIT_TEMPLATE.render(provider=provider))


def create_provider_datasources(provider, providerdir, datasources):

    with open(os.path.join(providerdir, 'd.py'), 'wt') as fp:
        fp.write(DATASOURCES_TEMPLATE.render(provider=provider, datasources=datasources))


def create_provider_resources(provider, providerdir, resources):
    logging.debug('create_provider_resources provider={}'.format(provider))
    logging.debug('create_provider_resources providerdir={}'.format(providerdir))
    for resource in resources:
        logging.debug('create_provider_resources resource={}'.format(resource))

    with open(os.path.join(providerdir, 'r.py'), 'wt') as fp:
        fp.write(RESOURCES_TEMPLATE.render(provider=provider, resources=resources))


def process(provider, modulesdir):

    print(provider)

    with tempfile.TemporaryDirectory() as tmpdir:

        cmd = 'git clone --depth=1 https://github.com/terraform-providers/terraform-provider-{} .'.format(provider)
        result = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=tmpdir)
        if result.returncode != 0:
            print(result.stdout)
            sys.exit(1)


        with open(os.path.join(tmpdir, provider, 'provider.go'), 'rb') as fp:
            content = fp.read()

            resources = []
            datasources = []

            for m in REGEX.finditer(content):

                name = m.groupdict()['name']

                if m.groupdict()['type'] == b'resource':
                    resources.append(name.decode())
                elif m.groupdict()['type'] == b'data':
                    datasources.append(name.decode())
                else:
                    # Shouldn't really get here.
                    pass

        providerdir = create_provider_directory(provider, modulesdir)
        create_provider_init(provider, providerdir)
        create_provider_datasources(provider, providerdir, datasources)
        create_provider_resources(provider, providerdir, resources)


def main():

    thisdir = os.path.abspath('.')
    rootdir = os.path.abspath('..')
    modulesdir = os.path.abspath('../terrascript')

    try:
        os.stat(os.path.join(thisdir, sys.argv[0]))
        os.stat(os.path.join(thisdir, 'PROVIDERS'))
    except FileNotFoundError:
        print('Script must be run from the tools/ folder', file=sys.stderr)
        sys.exit(1)

    # Detect whether a list of providers was passed on the command line or whether
    # to read PROVIDERS.
    #
    providers = sys.argv[1:]
    if not providers:
        providers = [line.strip() for line in open('PROVIDERS', 'rt').readlines() if line]

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(process, provider, modulesdir) for provider in providers]
        concurrent.futures.as_completed(futures)


if __name__ == '__main__':
    main()

