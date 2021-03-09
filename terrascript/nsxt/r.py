# terrascript/nsxt/r.py
import terrascript


class nsxt_dhcp_relay_profile(terrascript.Resource):
    pass


class nsxt_dhcp_relay_service(terrascript.Resource):
    pass


class nsxt_dhcp_server_profile(terrascript.Resource):
    pass


class nsxt_logical_dhcp_server(terrascript.Resource):
    pass


class nsxt_dhcp_server_ip_pool(terrascript.Resource):
    pass


class nsxt_logical_switch(terrascript.Resource):
    pass


class nsxt_vlan_logical_switch(terrascript.Resource):
    pass


class nsxt_logical_dhcp_port(terrascript.Resource):
    pass


class nsxt_logical_port(terrascript.Resource):
    pass


class nsxt_logical_tier0_router(terrascript.Resource):
    pass


class nsxt_logical_tier1_router(terrascript.Resource):
    pass


class nsxt_logical_router_centralized_service_port(terrascript.Resource):
    pass


class nsxt_logical_router_downlink_port(terrascript.Resource):
    pass


class nsxt_logical_router_link_port_on_tier0(terrascript.Resource):
    pass


class nsxt_logical_router_link_port_on_tier1(terrascript.Resource):
    pass


class nsxt_ip_discovery_switching_profile(terrascript.Resource):
    pass


class nsxt_mac_management_switching_profile(terrascript.Resource):
    pass


class nsxt_qos_switching_profile(terrascript.Resource):
    pass


class nsxt_spoofguard_switching_profile(terrascript.Resource):
    pass


class nsxt_switch_security_switching_profile(terrascript.Resource):
    pass


class nsxt_l4_port_set_ns_service(terrascript.Resource):
    pass


class nsxt_algorithm_type_ns_service(terrascript.Resource):
    pass


class nsxt_icmp_type_ns_service(terrascript.Resource):
    pass


class nsxt_igmp_type_ns_service(terrascript.Resource):
    pass


class nsxt_ether_type_ns_service(terrascript.Resource):
    pass


class nsxt_ip_protocol_ns_service(terrascript.Resource):
    pass


class nsxt_ns_service_group(terrascript.Resource):
    pass


class nsxt_ns_group(terrascript.Resource):
    pass


class nsxt_firewall_section(terrascript.Resource):
    pass


class nsxt_nat_rule(terrascript.Resource):
    pass


class nsxt_ip_block(terrascript.Resource):
    pass


class nsxt_ip_block_subnet(terrascript.Resource):
    pass


class nsxt_ip_pool(terrascript.Resource):
    pass


class nsxt_ip_pool_allocation_ip_address(terrascript.Resource):
    pass


class nsxt_ip_set(terrascript.Resource):
    pass


class nsxt_static_route(terrascript.Resource):
    pass


class nsxt_vm_tags(terrascript.Resource):
    pass


class nsxt_lb_icmp_monitor(terrascript.Resource):
    pass


class nsxt_lb_tcp_monitor(terrascript.Resource):
    pass


class nsxt_lb_udp_monitor(terrascript.Resource):
    pass


class nsxt_lb_http_monitor(terrascript.Resource):
    pass


class nsxt_lb_https_monitor(terrascript.Resource):
    pass


class nsxt_lb_passive_monitor(terrascript.Resource):
    pass


class nsxt_lb_pool(terrascript.Resource):
    pass


class nsxt_lb_tcp_virtual_server(terrascript.Resource):
    pass


class nsxt_lb_udp_virtual_server(terrascript.Resource):
    pass


class nsxt_lb_http_virtual_server(terrascript.Resource):
    pass


class nsxt_lb_http_forwarding_rule(terrascript.Resource):
    pass


class nsxt_lb_http_request_rewrite_rule(terrascript.Resource):
    pass


class nsxt_lb_http_response_rewrite_rule(terrascript.Resource):
    pass


class nsxt_lb_cookie_persistence_profile(terrascript.Resource):
    pass


class nsxt_lb_source_ip_persistence_profile(terrascript.Resource):
    pass


class nsxt_lb_client_ssl_profile(terrascript.Resource):
    pass


class nsxt_lb_server_ssl_profile(terrascript.Resource):
    pass


class nsxt_lb_service(terrascript.Resource):
    pass


class nsxt_lb_fast_tcp_application_profile(terrascript.Resource):
    pass


class nsxt_lb_fast_udp_application_profile(terrascript.Resource):
    pass


class nsxt_lb_http_application_profile(terrascript.Resource):
    pass


class nsxt_policy_tier1_gateway(terrascript.Resource):
    pass


class nsxt_policy_tier1_gateway_interface(terrascript.Resource):
    pass


class nsxt_policy_tier0_gateway(terrascript.Resource):
    pass


class nsxt_policy_tier0_gateway_interface(terrascript.Resource):
    pass


class nsxt_policy_tier0_gateway_ha_vip_config(terrascript.Resource):
    pass


class nsxt_policy_group(terrascript.Resource):
    pass


class nsxt_policy_domain(terrascript.Resource):
    pass


class nsxt_policy_security_policy(terrascript.Resource):
    pass


class nsxt_policy_service(terrascript.Resource):
    pass


class nsxt_policy_gateway_policy(terrascript.Resource):
    pass


class nsxt_policy_predefined_gateway_policy(terrascript.Resource):
    pass


class nsxt_policy_predefined_security_policy(terrascript.Resource):
    pass


class nsxt_policy_segment(terrascript.Resource):
    pass


class nsxt_policy_vlan_segment(terrascript.Resource):
    pass


class nsxt_policy_fixed_segment(terrascript.Resource):
    pass


class nsxt_policy_static_route(terrascript.Resource):
    pass


class nsxt_policy_gateway_prefix_list(terrascript.Resource):
    pass


class nsxt_policy_vm_tags(terrascript.Resource):
    pass


class nsxt_policy_nat_rule(terrascript.Resource):
    pass


class nsxt_policy_ip_block(terrascript.Resource):
    pass


class nsxt_policy_lb_pool(terrascript.Resource):
    pass


class nsxt_policy_ip_pool(terrascript.Resource):
    pass


class nsxt_policy_ip_pool_block_subnet(terrascript.Resource):
    pass


class nsxt_policy_ip_pool_static_subnet(terrascript.Resource):
    pass


class nsxt_policy_lb_service(terrascript.Resource):
    pass


class nsxt_policy_lb_virtual_server(terrascript.Resource):
    pass


class nsxt_policy_ip_address_allocation(terrascript.Resource):
    pass


class nsxt_policy_bgp_neighbor(terrascript.Resource):
    pass


class nsxt_policy_bgp_config(terrascript.Resource):
    pass


class nsxt_policy_dhcp_relay(terrascript.Resource):
    pass


class nsxt_policy_dhcp_server(terrascript.Resource):
    pass


class nsxt_policy_context_profile(terrascript.Resource):
    pass


class nsxt_policy_dhcp_v4_static_binding(terrascript.Resource):
    pass


class nsxt_policy_dhcp_v6_static_binding(terrascript.Resource):
    pass


class nsxt_policy_dns_forwarder_zone(terrascript.Resource):
    pass


class nsxt_policy_gateway_dns_forwarder(terrascript.Resource):
    pass


class nsxt_policy_gateway_community_list(terrascript.Resource):
    pass


class nsxt_policy_gateway_route_map(terrascript.Resource):
    pass


class nsxt_policy_intrusion_service_policy(terrascript.Resource):
    pass


class nsxt_policy_static_route_bfd_peer(terrascript.Resource):
    pass


class nsxt_policy_intrusion_service_profile(terrascript.Resource):
    pass


class nsxt_policy_evpn_tenant(terrascript.Resource):
    pass


class nsxt_policy_evpn_config(terrascript.Resource):
    pass


class nsxt_policy_evpn_tunnel_endpoint(terrascript.Resource):
    pass


class nsxt_policy_qos_profile(terrascript.Resource):
    pass


class nsxt_policy_ospf_config(terrascript.Resource):
    pass


class nsxt_policy_ospf_area(terrascript.Resource):
    pass
