# tests/test_provider_joyent_triton.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:29:19 UTC)


def test_provider_import():
    import terrascript.provider.joyent.triton


def test_resource_import():
    from terrascript.resource.joyent.triton import triton_fabric

    from terrascript.resource.joyent.triton import triton_firewall_rule

    from terrascript.resource.joyent.triton import triton_instance_template

    from terrascript.resource.joyent.triton import triton_key

    from terrascript.resource.joyent.triton import triton_machine

    from terrascript.resource.joyent.triton import triton_service_group

    from terrascript.resource.joyent.triton import triton_snapshot

    from terrascript.resource.joyent.triton import triton_vlan

    from terrascript.resource.joyent.triton import triton_volume


def test_datasource_import():
    from terrascript.data.joyent.triton import triton_account

    from terrascript.data.joyent.triton import triton_datacenter

    from terrascript.data.joyent.triton import triton_fabric_network

    from terrascript.data.joyent.triton import triton_fabric_vlan

    from terrascript.data.joyent.triton import triton_image

    from terrascript.data.joyent.triton import triton_network

    from terrascript.data.joyent.triton import triton_package

    from terrascript.data.joyent.triton import triton_volume


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.joyent.triton
#
#      t = terrascript.provider.joyent.triton.triton()
#      s = str(t)
#
#      assert 'https://github.com/joyent/terraform-provider-triton' in s
#      assert '0.8.2' in s
