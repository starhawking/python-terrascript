# tests/test_provider_DTherHtun_idm.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:19:03 UTC)


def test_provider_import():
    import terrascript.provider.DTherHtun.idm


def test_resource_import():
    from terrascript.resource.DTherHtun.idm import idm_dns_record

    from terrascript.resource.DTherHtun.idm import idm_host


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.DTherHtun.idm
#
#      t = terrascript.provider.DTherHtun.idm.idm()
#      s = str(t)
#
#      assert 'https://github.com/DTherHtun/terraform-provider-idm' in s
#      assert '0.0.2' in s
