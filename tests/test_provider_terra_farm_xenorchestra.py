# tests/test_provider_terra-farm_xenorchestra.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:31:20 UTC)


def test_provider_import():
    import terrascript.provider.terra_farm.xenorchestra


def test_resource_import():
    from terrascript.resource.terra_farm.xenorchestra import xenorchestra_acl

    from terrascript.resource.terra_farm.xenorchestra import xenorchestra_cloud_config

    from terrascript.resource.terra_farm.xenorchestra import xenorchestra_resource_set

    from terrascript.resource.terra_farm.xenorchestra import xenorchestra_vm


def test_datasource_import():
    from terrascript.data.terra_farm.xenorchestra import xenorchestra_cloud_config

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_host

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_hosts

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_network

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_pif

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_pool

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_resource_set

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_sr

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_template

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_user

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_vdi

    from terrascript.data.terra_farm.xenorchestra import xenorchestra_vms


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.terra_farm.xenorchestra
#
#      t = terrascript.provider.terra_farm.xenorchestra.xenorchestra()
#      s = str(t)
#
#      assert 'https://github.com/terra-farm/terraform-provider-xenorchestra' in s
#      assert '0.21.0' in s
