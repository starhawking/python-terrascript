# terrascript/resource/cloudscale.py

import terrascript


class cloudscale_server(terrascript.Resource):
    pass

class cloudscale_server_group(terrascript.Resource):
    pass

class cloudscale_volume(terrascript.Resource):
    pass

class cloudscale_network(terrascript.Resource):
    pass

class cloudscale_floating_ip(terrascript.Resource):
    pass


__all__ = [
    'cloudscale_server',
    'cloudscale_server_group',
    'cloudscale_volume',
    'cloudscale_network',
    'cloudscale_floating_ip',
]