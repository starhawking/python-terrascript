# tests/test_provider_apparentlymart_javascript.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:19:26 UTC)


def test_provider_import():
    import terrascript.provider.apparentlymart.javascript


def test_datasource_import():
    from terrascript.data.apparentlymart.javascript import javascript


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.apparentlymart.javascript
#
#      t = terrascript.provider.apparentlymart.javascript.javascript()
#      s = str(t)
#
#      assert 'https://github.com/apparentlymart/terraform-provider-javascript' in s
#      assert '0.0.1' in s