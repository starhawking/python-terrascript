# tests/test_provider_paultyng_null.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:33:28 UTC)


def test_provider_import():
    import terrascript.provider.paultyng.null


def test_resource_import():
    from terrascript.resource.paultyng.null import null_resource


def test_datasource_import():
    from terrascript.data.paultyng.null import null_data_source


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.paultyng.null
#
#      t = terrascript.provider.paultyng.null.null()
#      s = str(t)
#
#      assert 'https://github.com/paultyng/terraform-provider-null' in s
#      assert '0.1.1' in s
