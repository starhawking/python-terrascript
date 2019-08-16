from terrascript import Resource
class clc_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('clc_server', _label, **kwargs)
server = clc_server

class clc_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('clc_group', _label, **kwargs)
group = clc_group

class clc_public_ip(Resource):
    def __init__(self, _label, **kwargs): super().__init__('clc_public_ip', _label, **kwargs)
public_ip = clc_public_ip

class clc_load_balancer(Resource):
    def __init__(self, _label, **kwargs): super().__init__('clc_load_balancer', _label, **kwargs)
load_balancer = clc_load_balancer

class clc_load_balancer_pool(Resource):
    def __init__(self, _label, **kwargs): super().__init__('clc_load_balancer_pool', _label, **kwargs)
load_balancer_pool = clc_load_balancer_pool

