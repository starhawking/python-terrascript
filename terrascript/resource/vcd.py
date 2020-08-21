# terrascript/resource/vcd.py
import terrascript


class vcd_network(terrascript.Resource):
    pass


class vcd_network_routed(terrascript.Resource):
    pass


class vcd_network_direct(terrascript.Resource):
    pass


class vcd_network_isolated(terrascript.Resource):
    pass


class vcd_vapp_network(terrascript.Resource):
    pass


class vcd_vapp(terrascript.Resource):
    pass


class vcd_firewall_rules(terrascript.Resource):
    pass


class vcd_dnat(terrascript.Resource):
    pass


class vcd_snat(terrascript.Resource):
    pass


class vcd_edgegateway(terrascript.Resource):
    pass


class vcd_edgegateway_vpn(terrascript.Resource):
    pass


class vcd_vapp_vm(terrascript.Resource):
    pass


class vcd_org(terrascript.Resource):
    pass


class vcd_org_vdc(terrascript.Resource):
    pass


class vcd_org_user(terrascript.Resource):
    pass


class vcd_catalog(terrascript.Resource):
    pass


class vcd_catalog_item(terrascript.Resource):
    pass


class vcd_catalog_media(terrascript.Resource):
    pass


class vcd_inserted_media(terrascript.Resource):
    pass


class vcd_independent_disk(terrascript.Resource):
    pass


class vcd_external_network(terrascript.Resource):
    pass


class vcd_lb_service_monitor(terrascript.Resource):
    pass


class vcd_lb_server_pool(terrascript.Resource):
    pass


class vcd_lb_app_profile(terrascript.Resource):
    pass


class vcd_lb_app_rule(terrascript.Resource):
    pass


class vcd_lb_virtual_server(terrascript.Resource):
    pass


class vcd_nsxv_dnat(terrascript.Resource):
    pass


class vcd_nsxv_snat(terrascript.Resource):
    pass


class vcd_nsxv_firewall_rule(terrascript.Resource):
    pass


class vcd_nsxv_dhcp_relay(terrascript.Resource):
    pass


class vcd_nsxv_ip_set(terrascript.Resource):
    pass


class vcd_vm_internal_disk(terrascript.Resource):
    pass


class vcd_vapp_org_network(terrascript.Resource):
    pass


class vcd_org_group(terrascript.Resource):
    pass


class vcd_vapp_firewall_rules(terrascript.Resource):
    pass


class vcd_vapp_nat_rules(terrascript.Resource):
    pass


class vcd_vapp_static_routing(terrascript.Resource):
    pass


class vcd_vm_affinity_rule(terrascript.Resource):
    pass


__all__ = [
    "vcd_network",
    "vcd_network_routed",
    "vcd_network_direct",
    "vcd_network_isolated",
    "vcd_vapp_network",
    "vcd_vapp",
    "vcd_firewall_rules",
    "vcd_dnat",
    "vcd_snat",
    "vcd_edgegateway",
    "vcd_edgegateway_vpn",
    "vcd_vapp_vm",
    "vcd_org",
    "vcd_org_vdc",
    "vcd_org_user",
    "vcd_catalog",
    "vcd_catalog_item",
    "vcd_catalog_media",
    "vcd_inserted_media",
    "vcd_independent_disk",
    "vcd_external_network",
    "vcd_lb_service_monitor",
    "vcd_lb_server_pool",
    "vcd_lb_app_profile",
    "vcd_lb_app_rule",
    "vcd_lb_virtual_server",
    "vcd_nsxv_dnat",
    "vcd_nsxv_snat",
    "vcd_nsxv_firewall_rule",
    "vcd_nsxv_dhcp_relay",
    "vcd_nsxv_ip_set",
    "vcd_vm_internal_disk",
    "vcd_vapp_org_network",
    "vcd_org_group",
    "vcd_vapp_firewall_rules",
    "vcd_vapp_nat_rules",
    "vcd_vapp_static_routing",
    "vcd_vm_affinity_rule",
]
