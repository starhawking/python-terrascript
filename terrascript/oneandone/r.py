from terrascript import Resource
class oneandone_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_server', _label, **kwargs)
server = oneandone_server

class oneandone_firewall_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_firewall_policy', _label, **kwargs)
firewall_policy = oneandone_firewall_policy

class oneandone_private_network(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_private_network', _label, **kwargs)
private_network = oneandone_private_network

class oneandone_public_ip(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_public_ip', _label, **kwargs)
public_ip = oneandone_public_ip

class oneandone_shared_storage(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_shared_storage', _label, **kwargs)
shared_storage = oneandone_shared_storage

class oneandone_monitoring_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_monitoring_policy', _label, **kwargs)
monitoring_policy = oneandone_monitoring_policy

class oneandone_loadbalancer(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_loadbalancer', _label, **kwargs)
loadbalancer = oneandone_loadbalancer

class oneandone_vpn(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_vpn', _label, **kwargs)
vpn = oneandone_vpn

class oneandone_ssh_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_ssh_key', _label, **kwargs)
ssh_key = oneandone_ssh_key

class oneandone_block_storage(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_block_storage', _label, **kwargs)
block_storage = oneandone_block_storage

class oneandone_image(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_image', _label, **kwargs)
image = oneandone_image

class oneandone_baremetal(Resource):
    def __init__(self, _label, **kwargs): super().__init__('oneandone_baremetal', _label, **kwargs)
baremetal = oneandone_baremetal

