# tests/test_provider_sethvargo_filesystem.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:16:21 UTC)


def test_provider_import():
    import terrascript.provider.sethvargo.filesystem


def test_resource_import():
    from terrascript.resource.sethvargo.filesystem import filesystem_file_reader

    from terrascript.resource.sethvargo.filesystem import filesystem_file_writer


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.sethvargo.filesystem
#
#      t = terrascript.provider.sethvargo.filesystem.filesystem()
#      s = str(t)
#
#      assert 'https://github.com/sethvargo/terraform-provider-filesystem' in s
#      assert '0.2.0' in s
