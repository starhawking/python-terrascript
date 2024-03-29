# tests/test_provider_MissionCriticalCloud_cosmic.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:14:40 UTC)


def test_provider_import():
    import terrascript.provider.MissionCriticalCloud.cosmic


def test_resource_import():
    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_affinity_group

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_disk

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_instance

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_ipaddress

    from terrascript.resource.MissionCriticalCloud.cosmic import (
        cosmic_loadbalancer_rule,
    )

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_network

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_network_acl

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_network_acl_rule

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_nic

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_port_forward

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_private_gateway

    from terrascript.resource.MissionCriticalCloud.cosmic import (
        cosmic_secondary_ipaddress,
    )

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_ssh_keypair

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_static_nat

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_static_route

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_template

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_vpc

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_vpn_connection

    from terrascript.resource.MissionCriticalCloud.cosmic import (
        cosmic_vpn_customer_gateway,
    )

    from terrascript.resource.MissionCriticalCloud.cosmic import cosmic_vpn_gateway


def test_datasource_import():
    from terrascript.data.MissionCriticalCloud.cosmic import cosmic_network_acl


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.MissionCriticalCloud.cosmic
#
#      t = terrascript.provider.MissionCriticalCloud.cosmic.cosmic()
#      s = str(t)
#
#      assert 'https://github.com/MissionCriticalCloud/terraform-provider-cosmic' in s
#      assert '0.5.0' in s
