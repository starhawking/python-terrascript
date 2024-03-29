# tests/test_provider_strongdm_sdm.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:26:26 UTC)


def test_provider_import():
    import terrascript.provider.strongdm.sdm


def test_resource_import():
    from terrascript.resource.strongdm.sdm import sdm_account

    from terrascript.resource.strongdm.sdm import sdm_account_attachment

    from terrascript.resource.strongdm.sdm import sdm_account_grant

    from terrascript.resource.strongdm.sdm import sdm_node

    from terrascript.resource.strongdm.sdm import sdm_resource

    from terrascript.resource.strongdm.sdm import sdm_role

    from terrascript.resource.strongdm.sdm import sdm_role_attachment

    from terrascript.resource.strongdm.sdm import sdm_role_grant

    from terrascript.resource.strongdm.sdm import sdm_secret_store


def test_datasource_import():
    from terrascript.data.strongdm.sdm import sdm_account

    from terrascript.data.strongdm.sdm import sdm_account_attachment

    from terrascript.data.strongdm.sdm import sdm_account_grant

    from terrascript.data.strongdm.sdm import sdm_node

    from terrascript.data.strongdm.sdm import sdm_resource

    from terrascript.data.strongdm.sdm import sdm_role

    from terrascript.data.strongdm.sdm import sdm_role_attachment

    from terrascript.data.strongdm.sdm import sdm_role_grant

    from terrascript.data.strongdm.sdm import sdm_secret_store

    from terrascript.data.strongdm.sdm import sdm_ssh_ca_pubkey


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.strongdm.sdm
#
#      t = terrascript.provider.strongdm.sdm.sdm()
#      s = str(t)
#
#      assert 'https://github.com/strongdm/terraform-provider-sdm' in s
#      assert '1.0.28' in s
