# tests/test_provider_bltavares_zerotier.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:31:25 UTC)


def test_provider_import():
    import terrascript.provider.bltavares.zerotier


def test_resource_import():
    from terrascript.resource.bltavares.zerotier import zerotier_member

    from terrascript.resource.bltavares.zerotier import zerotier_network


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.bltavares.zerotier
#
#      t = terrascript.provider.bltavares.zerotier.zerotier()
#      s = str(t)
#
#      assert 'https://github.com/bltavares/terraform-provider-zerotier' in s
#      assert '0.3.0' in s
