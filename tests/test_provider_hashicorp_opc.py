# tests/test_provider_hashicorp_opc.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:23:41 UTC)


def test_provider_import():
    import terrascript.provider.hashicorp.opc


def test_resource_import():
    from terrascript.resource.hashicorp.opc import opc_compute_acl

    from terrascript.resource.hashicorp.opc import opc_compute_image_list

    from terrascript.resource.hashicorp.opc import opc_compute_image_list_entry

    from terrascript.resource.hashicorp.opc import opc_compute_instance

    from terrascript.resource.hashicorp.opc import opc_compute_ip_address_association

    from terrascript.resource.hashicorp.opc import opc_compute_ip_address_prefix_set

    from terrascript.resource.hashicorp.opc import opc_compute_ip_address_reservation

    from terrascript.resource.hashicorp.opc import opc_compute_ip_association

    from terrascript.resource.hashicorp.opc import opc_compute_ip_network

    from terrascript.resource.hashicorp.opc import opc_compute_ip_network_exchange

    from terrascript.resource.hashicorp.opc import opc_compute_ip_reservation

    from terrascript.resource.hashicorp.opc import opc_compute_machine_image

    from terrascript.resource.hashicorp.opc import opc_compute_orchestrated_instance

    from terrascript.resource.hashicorp.opc import opc_compute_route

    from terrascript.resource.hashicorp.opc import opc_compute_sec_rule

    from terrascript.resource.hashicorp.opc import opc_compute_security_application

    from terrascript.resource.hashicorp.opc import opc_compute_security_association

    from terrascript.resource.hashicorp.opc import opc_compute_security_ip_list

    from terrascript.resource.hashicorp.opc import opc_compute_security_list

    from terrascript.resource.hashicorp.opc import opc_compute_security_protocol

    from terrascript.resource.hashicorp.opc import opc_compute_security_rule

    from terrascript.resource.hashicorp.opc import opc_compute_snapshot

    from terrascript.resource.hashicorp.opc import opc_compute_ssh_key

    from terrascript.resource.hashicorp.opc import opc_compute_storage_attachment

    from terrascript.resource.hashicorp.opc import opc_compute_storage_volume

    from terrascript.resource.hashicorp.opc import opc_compute_storage_volume_snapshot

    from terrascript.resource.hashicorp.opc import opc_compute_vnic_set

    from terrascript.resource.hashicorp.opc import opc_compute_vpn_endpoint_v2

    from terrascript.resource.hashicorp.opc import opc_lbaas_certificate

    from terrascript.resource.hashicorp.opc import opc_lbaas_listener

    from terrascript.resource.hashicorp.opc import opc_lbaas_load_balancer

    from terrascript.resource.hashicorp.opc import opc_lbaas_policy

    from terrascript.resource.hashicorp.opc import opc_lbaas_server_pool

    from terrascript.resource.hashicorp.opc import opc_storage_container

    from terrascript.resource.hashicorp.opc import opc_storage_object


def test_datasource_import():
    from terrascript.data.hashicorp.opc import opc_compute_image_list_entry

    from terrascript.data.hashicorp.opc import opc_compute_ip_address_reservation

    from terrascript.data.hashicorp.opc import opc_compute_ip_reservation

    from terrascript.data.hashicorp.opc import opc_compute_machine_image

    from terrascript.data.hashicorp.opc import opc_compute_network_interface

    from terrascript.data.hashicorp.opc import opc_compute_ssh_key

    from terrascript.data.hashicorp.opc import opc_compute_storage_volume_snapshot

    from terrascript.data.hashicorp.opc import opc_compute_vnic


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.hashicorp.opc
#
#      t = terrascript.provider.hashicorp.opc.opc()
#      s = str(t)
#
#      assert 'https://github.com/terraform-providers/terraform-provider-opc' in s
#      assert '1.4.1' in s