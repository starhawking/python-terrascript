# tests/test_provider_hashicorp_cloudinit.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:14:09 UTC)


def test_provider_import():
    import terrascript.provider.hashicorp.cloudinit


def test_resource_import():
    from terrascript.resource.hashicorp.cloudinit import cloudinit_config


def test_datasource_import():
    from terrascript.data.hashicorp.cloudinit import cloudinit_config


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.hashicorp.cloudinit
#
#      t = terrascript.provider.hashicorp.cloudinit.cloudinit()
#      s = str(t)
#
#      assert 'https://github.com/hashicorp/terraform-provider-cloudinit' in s
#      assert '2.2.0' in s
