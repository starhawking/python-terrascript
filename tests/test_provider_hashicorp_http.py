# tests/test_provider_hashicorp_http.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:18:58 UTC)


def test_provider_import():
    import terrascript.provider.hashicorp.http


def test_datasource_import():
    from terrascript.data.hashicorp.http import http


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.hashicorp.http
#
#      t = terrascript.provider.hashicorp.http.http()
#      s = str(t)
#
#      assert 'https://github.com/hashicorp/terraform-provider-http' in s
#      assert '2.1.0' in s
