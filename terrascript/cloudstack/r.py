from terrascript import Resource
class cloudstack_affinity_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_affinity_group', _label, **kwargs)
affinity_group = cloudstack_affinity_group

class cloudstack_disk(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_disk', _label, **kwargs)
disk = cloudstack_disk

class cloudstack_egress_firewall(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_egress_firewall', _label, **kwargs)
egress_firewall = cloudstack_egress_firewall

class cloudstack_firewall(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_firewall', _label, **kwargs)
firewall = cloudstack_firewall

class cloudstack_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_instance', _label, **kwargs)
instance = cloudstack_instance

class cloudstack_ipaddress(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_ipaddress', _label, **kwargs)
ipaddress = cloudstack_ipaddress

class cloudstack_loadbalancer_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_loadbalancer_rule', _label, **kwargs)
loadbalancer_rule = cloudstack_loadbalancer_rule

class cloudstack_network(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_network', _label, **kwargs)
network = cloudstack_network

class cloudstack_network_acl(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_network_acl', _label, **kwargs)
network_acl = cloudstack_network_acl

class cloudstack_network_acl_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_network_acl_rule', _label, **kwargs)
network_acl_rule = cloudstack_network_acl_rule

class cloudstack_nic(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_nic', _label, **kwargs)
nic = cloudstack_nic

class cloudstack_port_forward(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_port_forward', _label, **kwargs)
port_forward = cloudstack_port_forward

class cloudstack_private_gateway(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_private_gateway', _label, **kwargs)
private_gateway = cloudstack_private_gateway

class cloudstack_secondary_ipaddress(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_secondary_ipaddress', _label, **kwargs)
secondary_ipaddress = cloudstack_secondary_ipaddress

class cloudstack_security_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_security_group', _label, **kwargs)
security_group = cloudstack_security_group

class cloudstack_security_group_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_security_group_rule', _label, **kwargs)
security_group_rule = cloudstack_security_group_rule

class cloudstack_ssh_keypair(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_ssh_keypair', _label, **kwargs)
ssh_keypair = cloudstack_ssh_keypair

class cloudstack_static_nat(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_static_nat', _label, **kwargs)
static_nat = cloudstack_static_nat

class cloudstack_static_route(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_static_route', _label, **kwargs)
static_route = cloudstack_static_route

class cloudstack_template(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_template', _label, **kwargs)
template = cloudstack_template

class cloudstack_vpc(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_vpc', _label, **kwargs)
vpc = cloudstack_vpc

class cloudstack_vpn_connection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_vpn_connection', _label, **kwargs)
vpn_connection = cloudstack_vpn_connection

class cloudstack_vpn_customer_gateway(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_vpn_customer_gateway', _label, **kwargs)
vpn_customer_gateway = cloudstack_vpn_customer_gateway

class cloudstack_vpn_gateway(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudstack_vpn_gateway', _label, **kwargs)
vpn_gateway = cloudstack_vpn_gateway

