# tests/test_provider_mrcrilly_awx.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:12:44 UTC)


def test_provider_import():
    import terrascript.provider.mrcrilly.awx


def test_resource_import():
    from terrascript.resource.mrcrilly.awx import awx_credential_azure_key_vault

    from terrascript.resource.mrcrilly.awx import awx_credential_input_source

    from terrascript.resource.mrcrilly.awx import awx_credential_machine


def test_datasource_import():
    from terrascript.data.mrcrilly.awx import awx_credential

    from terrascript.data.mrcrilly.awx import awx_credential_azure_key_vault

    from terrascript.data.mrcrilly.awx import awx_credentials


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.mrcrilly.awx
#
#      t = terrascript.provider.mrcrilly.awx.awx()
#      s = str(t)
#
#      assert 'https://github.com/mrcrilly/terraform-provider-awx' in s
#      assert '0.1.2' in s
