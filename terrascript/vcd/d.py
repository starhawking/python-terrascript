# terrascript/vcd/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class vcd_catalog(terrascript.Data):
    pass


class vcd_catalog_item(terrascript.Data):
    pass


class vcd_catalog_media(terrascript.Data):
    pass


class vcd_edgegateway(terrascript.Data):
    pass


class vcd_external_network(terrascript.Data):
    pass


class vcd_external_network_v2(terrascript.Data):
    pass


class vcd_independent_disk(terrascript.Data):
    pass


class vcd_lb_app_profile(terrascript.Data):
    pass


class vcd_lb_app_rule(terrascript.Data):
    pass


class vcd_lb_server_pool(terrascript.Data):
    pass


class vcd_lb_service_monitor(terrascript.Data):
    pass


class vcd_lb_virtual_server(terrascript.Data):
    pass


class vcd_network_direct(terrascript.Data):
    pass


class vcd_network_isolated(terrascript.Data):
    pass


class vcd_network_routed(terrascript.Data):
    pass


class vcd_nsxt_edge_cluster(terrascript.Data):
    pass


class vcd_nsxt_edgegateway(terrascript.Data):
    pass


class vcd_nsxt_manager(terrascript.Data):
    pass


class vcd_nsxt_tier0_router(terrascript.Data):
    pass


class vcd_nsxv_dhcp_relay(terrascript.Data):
    pass


class vcd_nsxv_dnat(terrascript.Data):
    pass


class vcd_nsxv_firewall_rule(terrascript.Data):
    pass


class vcd_nsxv_ip_set(terrascript.Data):
    pass


class vcd_nsxv_snat(terrascript.Data):
    pass


class vcd_org(terrascript.Data):
    pass


class vcd_org_user(terrascript.Data):
    pass


class vcd_org_vdc(terrascript.Data):
    pass


class vcd_portgroup(terrascript.Data):
    pass


class vcd_resource_list(terrascript.Data):
    pass


class vcd_resource_schema(terrascript.Data):
    pass


class vcd_storage_profile(terrascript.Data):
    pass


class vcd_vapp(terrascript.Data):
    pass


class vcd_vapp_network(terrascript.Data):
    pass


class vcd_vapp_org_network(terrascript.Data):
    pass


class vcd_vapp_vm(terrascript.Data):
    pass


class vcd_vcenter(terrascript.Data):
    pass


class vcd_vm_affinity_rule(terrascript.Data):
    pass


class vcd_vm_sizing_policy(terrascript.Data):
    pass
