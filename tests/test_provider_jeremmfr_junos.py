# tests/test_provider_jeremmfr_junos.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:19:45 UTC)


def test_provider_import():
    import terrascript.provider.jeremmfr.junos


def test_resource_import():
    from terrascript.resource.jeremmfr.junos import junos_aggregate_route

    from terrascript.resource.jeremmfr.junos import junos_application

    from terrascript.resource.jeremmfr.junos import junos_application_set

    from terrascript.resource.jeremmfr.junos import junos_bgp_group

    from terrascript.resource.jeremmfr.junos import junos_bgp_neighbor

    from terrascript.resource.jeremmfr.junos import junos_bridge_domain

    from terrascript.resource.jeremmfr.junos import junos_chassis_cluster

    from terrascript.resource.jeremmfr.junos import junos_eventoptions_destination

    from terrascript.resource.jeremmfr.junos import junos_eventoptions_generate_event

    from terrascript.resource.jeremmfr.junos import junos_eventoptions_policy

    from terrascript.resource.jeremmfr.junos import junos_evpn

    from terrascript.resource.jeremmfr.junos import junos_firewall_filter

    from terrascript.resource.jeremmfr.junos import junos_firewall_policer

    from terrascript.resource.jeremmfr.junos import (
        junos_forwardingoptions_sampling_instance,
    )

    from terrascript.resource.jeremmfr.junos import junos_generate_route

    from terrascript.resource.jeremmfr.junos import junos_group_dual_system

    from terrascript.resource.jeremmfr.junos import junos_interface

    from terrascript.resource.jeremmfr.junos import junos_interface_logical

    from terrascript.resource.jeremmfr.junos import junos_interface_physical

    from terrascript.resource.jeremmfr.junos import junos_interface_st0_unit

    from terrascript.resource.jeremmfr.junos import junos_null_commit_file

    from terrascript.resource.jeremmfr.junos import junos_ospf

    from terrascript.resource.jeremmfr.junos import junos_ospf_area

    from terrascript.resource.jeremmfr.junos import junos_policyoptions_as_path

    from terrascript.resource.jeremmfr.junos import junos_policyoptions_as_path_group

    from terrascript.resource.jeremmfr.junos import junos_policyoptions_community

    from terrascript.resource.jeremmfr.junos import junos_policyoptions_policy_statement

    from terrascript.resource.jeremmfr.junos import junos_policyoptions_prefix_list

    from terrascript.resource.jeremmfr.junos import junos_rib_group

    from terrascript.resource.jeremmfr.junos import junos_routing_instance

    from terrascript.resource.jeremmfr.junos import junos_routing_options

    from terrascript.resource.jeremmfr.junos import junos_security

    from terrascript.resource.jeremmfr.junos import junos_security_address_book

    from terrascript.resource.jeremmfr.junos import (
        junos_security_dynamic_address_feed_server,
    )

    from terrascript.resource.jeremmfr.junos import junos_security_dynamic_address_name

    from terrascript.resource.jeremmfr.junos import junos_security_global_policy

    from terrascript.resource.jeremmfr.junos import junos_security_idp_custom_attack

    from terrascript.resource.jeremmfr.junos import (
        junos_security_idp_custom_attack_group,
    )

    from terrascript.resource.jeremmfr.junos import junos_security_idp_policy

    from terrascript.resource.jeremmfr.junos import junos_security_ike_gateway

    from terrascript.resource.jeremmfr.junos import junos_security_ike_policy

    from terrascript.resource.jeremmfr.junos import junos_security_ike_proposal

    from terrascript.resource.jeremmfr.junos import junos_security_ipsec_policy

    from terrascript.resource.jeremmfr.junos import junos_security_ipsec_proposal

    from terrascript.resource.jeremmfr.junos import junos_security_ipsec_vpn

    from terrascript.resource.jeremmfr.junos import junos_security_log_stream

    from terrascript.resource.jeremmfr.junos import junos_security_nat_destination

    from terrascript.resource.jeremmfr.junos import junos_security_nat_destination_pool

    from terrascript.resource.jeremmfr.junos import junos_security_nat_source

    from terrascript.resource.jeremmfr.junos import junos_security_nat_source_pool

    from terrascript.resource.jeremmfr.junos import junos_security_nat_static

    from terrascript.resource.jeremmfr.junos import junos_security_policy

    from terrascript.resource.jeremmfr.junos import (
        junos_security_policy_tunnel_pair_policy,
    )

    from terrascript.resource.jeremmfr.junos import junos_security_screen

    from terrascript.resource.jeremmfr.junos import junos_security_screen_whitelist

    from terrascript.resource.jeremmfr.junos import (
        junos_security_utm_custom_url_category,
    )

    from terrascript.resource.jeremmfr.junos import (
        junos_security_utm_custom_url_pattern,
    )

    from terrascript.resource.jeremmfr.junos import junos_security_utm_policy

    from terrascript.resource.jeremmfr.junos import (
        junos_security_utm_profile_web_filtering_juniper_enhanced,
    )

    from terrascript.resource.jeremmfr.junos import (
        junos_security_utm_profile_web_filtering_juniper_local,
    )

    from terrascript.resource.jeremmfr.junos import (
        junos_security_utm_profile_web_filtering_websense_redirect,
    )

    from terrascript.resource.jeremmfr.junos import junos_security_zone

    from terrascript.resource.jeremmfr.junos import junos_security_zone_book_address

    from terrascript.resource.jeremmfr.junos import junos_security_zone_book_address_set

    from terrascript.resource.jeremmfr.junos import junos_services

    from terrascript.resource.jeremmfr.junos import (
        junos_services_advanced_anti_malware_policy,
    )

    from terrascript.resource.jeremmfr.junos import (
        junos_services_flowmonitoring_vipfix_template,
    )

    from terrascript.resource.jeremmfr.junos import junos_services_proxy_profile

    from terrascript.resource.jeremmfr.junos import junos_services_rpm_probe

    from terrascript.resource.jeremmfr.junos import (
        junos_services_security_intelligence_policy,
    )

    from terrascript.resource.jeremmfr.junos import (
        junos_services_security_intelligence_profile,
    )

    from terrascript.resource.jeremmfr.junos import (
        junos_services_ssl_initiation_profile,
    )

    from terrascript.resource.jeremmfr.junos import (
        junos_services_user_identification_ad_access_domain,
    )

    from terrascript.resource.jeremmfr.junos import (
        junos_services_user_identification_device_identity_profile,
    )

    from terrascript.resource.jeremmfr.junos import junos_snmp

    from terrascript.resource.jeremmfr.junos import junos_snmp_clientlist

    from terrascript.resource.jeremmfr.junos import junos_snmp_community

    from terrascript.resource.jeremmfr.junos import junos_snmp_view

    from terrascript.resource.jeremmfr.junos import junos_static_route

    from terrascript.resource.jeremmfr.junos import junos_switch_options

    from terrascript.resource.jeremmfr.junos import junos_system

    from terrascript.resource.jeremmfr.junos import junos_system_login_class

    from terrascript.resource.jeremmfr.junos import junos_system_login_user

    from terrascript.resource.jeremmfr.junos import junos_system_ntp_server

    from terrascript.resource.jeremmfr.junos import junos_system_radius_server

    from terrascript.resource.jeremmfr.junos import junos_system_root_authentication

    from terrascript.resource.jeremmfr.junos import junos_system_syslog_file

    from terrascript.resource.jeremmfr.junos import junos_system_syslog_host

    from terrascript.resource.jeremmfr.junos import junos_vlan


def test_datasource_import():
    from terrascript.data.jeremmfr.junos import junos_interface

    from terrascript.data.jeremmfr.junos import junos_interface_logical

    from terrascript.data.jeremmfr.junos import junos_interface_physical

    from terrascript.data.jeremmfr.junos import junos_system_information


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.jeremmfr.junos
#
#      t = terrascript.provider.jeremmfr.junos.junos()
#      s = str(t)
#
#      assert 'https://github.com/jeremmfr/terraform-provider-junos' in s
#      assert '1.20.0' in s
