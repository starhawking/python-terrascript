# tests/test_provider_stackpath_stackpath.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:27:49 UTC)


def test_provider_import():
    import terrascript.provider.stackpath.stackpath


def test_resource_import():
    from terrascript.resource.stackpath.stackpath import (
        stackpath_compute_network_policy,
    )

    from terrascript.resource.stackpath.stackpath import stackpath_compute_workload

    from terrascript.resource.stackpath.stackpath import stackpath_object_storage_bucket


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.stackpath.stackpath
#
#      t = terrascript.provider.stackpath.stackpath.stackpath()
#      s = str(t)
#
#      assert 'https://github.com/stackpath/terraform-provider-stackpath' in s
#      assert '1.3.3' in s