# tests/test_provider_carlpett_sops.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:27:24 UTC)


def test_provider_import():
    import terrascript.provider.carlpett.sops


def test_datasource_import():
    from terrascript.data.carlpett.sops import sops_external

    from terrascript.data.carlpett.sops import sops_file


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.carlpett.sops
#
#      t = terrascript.provider.carlpett.sops.sops()
#      s = str(t)
#
#      assert 'https://github.com/carlpett/terraform-provider-sops' in s
#      assert '0.6.3' in s
