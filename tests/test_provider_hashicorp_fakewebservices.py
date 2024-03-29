# tests/test_provider_hashicorp_fakewebservices.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:16:12 UTC)


def test_provider_import():
    import terrascript.provider.hashicorp.fakewebservices


def test_resource_import():
    from terrascript.resource.hashicorp.fakewebservices import fakewebservices_database

    from terrascript.resource.hashicorp.fakewebservices import (
        fakewebservices_load_balancer,
    )

    from terrascript.resource.hashicorp.fakewebservices import fakewebservices_server

    from terrascript.resource.hashicorp.fakewebservices import fakewebservices_vpc


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.hashicorp.fakewebservices
#
#      t = terrascript.provider.hashicorp.fakewebservices.fakewebservices()
#      s = str(t)
#
#      assert 'https://github.com/hashicorp/terraform-provider-fakewebservices' in s
#      assert '0.2.1' in s
