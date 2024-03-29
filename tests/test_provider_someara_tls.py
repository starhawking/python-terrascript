# tests/test_provider_someara_tls.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:28:55 UTC)


def test_provider_import():
    import terrascript.provider.someara.tls


def test_resource_import():
    from terrascript.resource.someara.tls import tls_cert_request

    from terrascript.resource.someara.tls import tls_locally_signed_cert

    from terrascript.resource.someara.tls import tls_private_key

    from terrascript.resource.someara.tls import tls_self_signed_cert


def test_datasource_import():
    from terrascript.data.someara.tls import tls_certificate

    from terrascript.data.someara.tls import tls_public_key


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.someara.tls
#
#      t = terrascript.provider.someara.tls.tls()
#      s = str(t)
#
#      assert 'https://github.com/someara/terraform-provider-tls' in s
#      assert '2.3.0-pre' in s
