from terrascript import Resource
class cloudscale_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudscale_server', _label, **kwargs)
server = cloudscale_server

class cloudscale_server_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudscale_server_group', _label, **kwargs)
server_group = cloudscale_server_group

class cloudscale_volume(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudscale_volume', _label, **kwargs)
volume = cloudscale_volume

class cloudscale_floating_ip(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cloudscale_floating_ip', _label, **kwargs)
floating_ip = cloudscale_floating_ip

