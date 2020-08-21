#!/usr/bin/env python3
"""Auto-generate provider specific modules.

   The script reads a list of Terraform providers from the file PROVIDERS, 
   pulls the provider's Github repository and parses the provider.go file.

   This script relies on the content of a provider's 'provider.go'
   matching the regular expression `REGEX` below.
   
   Runtime: 2:30 minutes

   Changelog:
   2020-08-21 - Cleaned up code to conform to pep8
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
import concurrent.futures
import logging
import os
import os.path
import re
import shlex
import subprocess
import sys
import tempfile

import jinja2
import yaml

DEBUG = False
CONCURRENCY = 10
INPUT = "providers.yml"

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

LEGACY_INIT_TEMPLATE = jinja2.Template(
    """# terrascript/{{ provider }}/__init__.py
import terrascript


class {{ provider }}(terrascript.Provider):
    pass

"""
)

LEGACY_DATASOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/{{ provider }}/d.py
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
    """# terrascript/{{ provider }}/r.py
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
    """# terrascript/provider/{{ provider }}.py
import terrascript


class {{ provider }}(terrascript.Provider):
    pass


__all__ = ["{{ provider }}"]

"""
)

RESOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/resource/{{ provider }}.py
{%- if resources %}
import terrascript
{%- endif -%}
{%- for resource in resources %}


class {{ resource }}(terrascript.Resource):
    pass
{%- endfor %}


__all__ = [{% if resources -%}
{%- for resource in resources %}
    "{{ resource }}",
{%- endfor %}
{% endif %}]

"""
)

DATASOURCES_TEMPLATE = jinja2.Template(
    """# terrascript/data/{{ provider }}.py
{%- if datasources %}
import terrascript
{%- endif -%}
{%- for datasource in datasources %}


class {{ datasource }}(terrascript.Data):
    pass
{%- endfor %}


__all__ = [{% if datasources -%}
{%- for datasource in datasources %}
    "{{ datasource }}",
{%- endfor %}
{% endif %}]

"""
)

INIT_TEMPLATE = jinja2.Template(
    """# terrascript/*/__init__.py
from .terraform import *
{%- for provider in providers %}
from .{{ provider }} import *
{%- endfor %}

"""
)


def legacy_create_provider_directory(provider, modulesdir):
    providerdir = os.path.join(modulesdir, provider)

    if not os.path.isdir(providerdir):
        os.mkdir(providerdir)

    return providerdir


def legacy_create_provider_init(provider, providerdir):
    with open(os.path.join(providerdir, "__init__.py"), "wt") as fp:
        fp.write(LEGACY_INIT_TEMPLATE.render(provider=provider))


def legacy_create_provider_datasources(provider, providerdir, datasources):
    with open(os.path.join(providerdir, "d.py"), "wt") as fp:
        fp.write(
            LEGACY_DATASOURCES_TEMPLATE.render(
                provider=provider, datasources=datasources
            )
        )


def legacy_create_provider_resources(provider, providerdir, resources):
    logging.debug("legacy_create_provider_resources provider={}".format(provider))
    logging.debug("legacy_create_provider_resources providerdir={}".format(providerdir))
    for resource in resources:
        logging.debug("legacy_create_provider_resources resource={}".format(resource))

    with open(os.path.join(providerdir, "r.py"), "wt") as fp:
        fp.write(
            LEGACY_RESOURCES_TEMPLATE.render(provider=provider, resources=resources)
        )


def legacy_process(provider, modulesdir, resources, datasources):
    legacy_providerdir = legacy_create_provider_directory(provider, modulesdir)
    legacy_create_provider_init(provider, legacy_providerdir)
    legacy_create_provider_datasources(provider, legacy_providerdir, datasources)
    legacy_create_provider_resources(provider, legacy_providerdir, resources)


def create_provider(provider, modulesdir):
    logging.debug("create_provider provider=%s modulesdir=%s", provider, modulesdir)
    with open(os.path.join(modulesdir, "provider", "{}.py".format(provider)), "wt") as fp:
        fp.write(PROVIDER_TEMPLATE.render(provider=provider))


def create_resources(provider, modulesdir, resources):
    with open(os.path.join(modulesdir, "resource", "{}.py".format(provider)), "wt") as fp:
        fp.write(RESOURCES_TEMPLATE.render(provider=provider, resources=resources))


def create_datasources(provider, modulesdir, datasources):
    with open(os.path.join(modulesdir, "data", "{}.py".format(provider)), "wt") as fp:
        fp.write(
            DATASOURCES_TEMPLATE.render(provider=provider, datasources=datasources)
        )


def process(entry, modulesdir):
    provider = entry["name"]
    repository = entry.get(
        "repository",
        "https://github.com/terraform-providers/terraform-provider-{}".format(provider),
    )
    logging.info(provider)

    with tempfile.TemporaryDirectory() as tmpdir:

        cmd = "git clone --depth=1 {} .".format(repository)
        result = subprocess.run(
            shlex.split(cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=tmpdir,
        )
        if result.returncode != 0:
            print(result.stdout)
            sys.exit(1)

        with open(os.path.join(tmpdir, provider, "provider.go"), "rb") as fp:
            content = fp.read()

            resources = []
            datasources = []

            for m in REGEX.finditer(content):

                name = m.groupdict()["name"]

                if m.groupdict()["type"] == b"resource":
                    resources.append(name.decode())
                elif m.groupdict()["type"] == b"data":
                    datasources.append(name.decode())
                else:
                    # Shouldn't really get here.
                    pass

        # The legacy layout creates
        #
        # PROVIDER/__init__.py
        # PROVIDER/r/py
        # PROVIDER/d/py
        #
        legacy_process(provider, modulesdir, resources, datasources)

        # The new layout creates
        #
        # providers/PROVIDER.py
        # resources/PROVIDER.py
        # datasources/PROVIDER.py
        #
        create_provider(provider, modulesdir)
        create_resources(provider, modulesdir, resources)
        create_datasources(provider, modulesdir, datasources)


def main():
    thisdir = os.path.abspath(".")
    # rootdir = os.path.abspath("..")
    modulesdir = os.path.abspath("../terrascript")

    try:
        os.stat(os.path.join(thisdir, sys.argv[0]))
        os.stat(os.path.join(thisdir, INPUT))
    except FileNotFoundError:
        print("Script must be run from the tools/ folder", file=sys.stderr)
        sys.exit(1)

    with open(INPUT, "rt") as fp:
        entries = yaml.load(fp, Loader=yaml.SafeLoader)
        # entries is now a list of dictionaries: [{'name': NAME, 'repository': URL}, ...]

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(process, entry, modulesdir) for entry in entries]
        for future in concurrent.futures.as_completed(futures):
            exc = future.exception()
            if exc:
                raise exc

    # Create the __ini__.py files for providers, datasources and resources.
    #
    providers = [entry["name"] for entry in entries]
    with open(os.path.join(modulesdir, "provider", "__init__.py"), "wt") as fp:
        fp.write(INIT_TEMPLATE.render(providers=providers))

    with open(os.path.join(modulesdir, "resource", "__init__.py"), "wt") as fp:
        fp.write(INIT_TEMPLATE.render(providers=providers))

    with open(os.path.join(modulesdir, "data", "__init__.py"), "wt") as fp:
        fp.write(INIT_TEMPLATE.render(providers=providers))


if __name__ == "__main__":
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    main()
