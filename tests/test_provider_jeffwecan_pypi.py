# tests/test_provider_jeffwecan_pypi.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:25:16 UTC)


def test_provider_import():
    import terrascript.provider.jeffwecan.pypi


def test_datasource_import():
    from terrascript.data.jeffwecan.pypi import pypi_package_file

    from terrascript.data.jeffwecan.pypi import pypi_requirements_file


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.jeffwecan.pypi
#
#      t = terrascript.provider.jeffwecan.pypi.pypi()
#      s = str(t)
#
#      assert 'https://github.com/jeffwecan/terraform-provider-pypi' in s
#      assert '0.0.9' in s
