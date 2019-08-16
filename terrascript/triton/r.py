from terrascript import Resource
class triton_fabric(Resource):
    def __init__(self, _label, **kwargs): super().__init__('triton_fabric', _label, **kwargs)
fabric = triton_fabric

class triton_firewall_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('triton_firewall_rule', _label, **kwargs)
firewall_rule = triton_firewall_rule

class triton_instance_template(Resource):
    def __init__(self, _label, **kwargs): super().__init__('triton_instance_template', _label, **kwargs)
instance_template = triton_instance_template

class triton_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('triton_key', _label, **kwargs)
key = triton_key

class triton_machine(Resource):
    def __init__(self, _label, **kwargs): super().__init__('triton_machine', _label, **kwargs)
machine = triton_machine

class triton_service_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('triton_service_group', _label, **kwargs)
service_group = triton_service_group

class triton_snapshot(Resource):
    def __init__(self, _label, **kwargs): super().__init__('triton_snapshot', _label, **kwargs)
snapshot = triton_snapshot

class triton_vlan(Resource):
    def __init__(self, _label, **kwargs): super().__init__('triton_vlan', _label, **kwargs)
vlan = triton_vlan

