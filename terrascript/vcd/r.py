from terrascript import Resource
class vcd_network(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_network', _label, **kwargs)
network = vcd_network

class vcd_network_routed(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_network_routed', _label, **kwargs)
network_routed = vcd_network_routed

class vcd_network_direct(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_network_direct', _label, **kwargs)
network_direct = vcd_network_direct

class vcd_network_isolated(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_network_isolated', _label, **kwargs)
network_isolated = vcd_network_isolated

class vcd_vapp_network(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_vapp_network', _label, **kwargs)
vapp_network = vcd_vapp_network

class vcd_vapp(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_vapp', _label, **kwargs)
vapp = vcd_vapp

class vcd_firewall_rules(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_firewall_rules', _label, **kwargs)
firewall_rules = vcd_firewall_rules

class vcd_dnat(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_dnat', _label, **kwargs)
dnat = vcd_dnat

class vcd_snat(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_snat', _label, **kwargs)
snat = vcd_snat

class vcd_edgegateway(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_edgegateway', _label, **kwargs)
edgegateway = vcd_edgegateway

class vcd_edgegateway_vpn(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_edgegateway_vpn', _label, **kwargs)
edgegateway_vpn = vcd_edgegateway_vpn

class vcd_vapp_vm(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_vapp_vm', _label, **kwargs)
vapp_vm = vcd_vapp_vm

class vcd_org(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_org', _label, **kwargs)
org = vcd_org

class vcd_org_vdc(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_org_vdc', _label, **kwargs)
org_vdc = vcd_org_vdc

class vcd_org_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_org_user', _label, **kwargs)
org_user = vcd_org_user

class vcd_catalog(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_catalog', _label, **kwargs)
catalog = vcd_catalog

class vcd_catalog_item(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_catalog_item', _label, **kwargs)
catalog_item = vcd_catalog_item

class vcd_catalog_media(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_catalog_media', _label, **kwargs)
catalog_media = vcd_catalog_media

class vcd_inserted_media(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_inserted_media', _label, **kwargs)
inserted_media = vcd_inserted_media

class vcd_independent_disk(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_independent_disk', _label, **kwargs)
independent_disk = vcd_independent_disk

class vcd_external_network(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_external_network', _label, **kwargs)
external_network = vcd_external_network

class vcd_lb_service_monitor(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_service_monitor', _label, **kwargs)
lb_service_monitor = vcd_lb_service_monitor

class vcd_lb_server_pool(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_server_pool', _label, **kwargs)
lb_server_pool = vcd_lb_server_pool

class vcd_lb_app_profile(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_app_profile', _label, **kwargs)
lb_app_profile = vcd_lb_app_profile

class vcd_lb_app_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_app_rule', _label, **kwargs)
lb_app_rule = vcd_lb_app_rule

class vcd_lb_virtual_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_virtual_server', _label, **kwargs)
lb_virtual_server = vcd_lb_virtual_server

