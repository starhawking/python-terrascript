from terrascript import Resource
class packet_device(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_device', _label, **kwargs)
device = packet_device

class packet_ssh_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_ssh_key', _label, **kwargs)
ssh_key = packet_ssh_key

class packet_project_ssh_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_project_ssh_key', _label, **kwargs)
project_ssh_key = packet_project_ssh_key

class packet_project(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_project', _label, **kwargs)
project = packet_project

class packet_organization(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_organization', _label, **kwargs)
organization = packet_organization

class packet_volume(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_volume', _label, **kwargs)
volume = packet_volume

class packet_volume_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_volume_attachment', _label, **kwargs)
volume_attachment = packet_volume_attachment

class packet_reserved_ip_block(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_reserved_ip_block', _label, **kwargs)
reserved_ip_block = packet_reserved_ip_block

class packet_ip_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_ip_attachment', _label, **kwargs)
ip_attachment = packet_ip_attachment

class packet_spot_market_request(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_spot_market_request', _label, **kwargs)
spot_market_request = packet_spot_market_request

class packet_vlan(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_vlan', _label, **kwargs)
vlan = packet_vlan

class packet_bgp_session(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_bgp_session', _label, **kwargs)
bgp_session = packet_bgp_session

class packet_port_vlan_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_port_vlan_attachment', _label, **kwargs)
port_vlan_attachment = packet_port_vlan_attachment

class packet_connect(Resource):
    def __init__(self, _label, **kwargs): super().__init__('packet_connect', _label, **kwargs)
connect = packet_connect

