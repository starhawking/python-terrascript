# tests/test_provider_paultyng_gsuite.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:17:49 UTC)


def test_provider_import():
    import terrascript.provider.paultyng.gsuite


def test_datasource_import():
    from terrascript.data.paultyng.gsuite import gsuite_sheets_spreadsheet_values


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.paultyng.gsuite
#
#      t = terrascript.provider.paultyng.gsuite.gsuite()
#      s = str(t)
#
#      assert 'https://github.com/paultyng/terraform-provider-gsuite' in s
#      assert '0.2.2' in s
