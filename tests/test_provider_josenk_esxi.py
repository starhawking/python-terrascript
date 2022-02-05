# tests/test_provider_josenk_esxi.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:15:57 UTC)


def test_provider_import():
    import terrascript.provider.josenk.esxi


def test_resource_import():
    from terrascript.resource.josenk.esxi import esxi_guest

    from terrascript.resource.josenk.esxi import esxi_portgroup

    from terrascript.resource.josenk.esxi import esxi_resource_pool

    from terrascript.resource.josenk.esxi import esxi_virtual_disk

    from terrascript.resource.josenk.esxi import esxi_vswitch


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.josenk.esxi
#
#      t = terrascript.provider.josenk.esxi.esxi()
#      s = str(t)
#
#      assert 'https://github.com/josenk/terraform-provider-esxi' in s
#      assert '1.8.3' in s