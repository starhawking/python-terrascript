# terrascript/resource/clc.py
import terrascript


class clc_server(terrascript.Resource):
    pass


class clc_group(terrascript.Resource):
    pass


class clc_public_ip(terrascript.Resource):
    pass


class clc_load_balancer(terrascript.Resource):
    pass


class clc_load_balancer_pool(terrascript.Resource):
    pass


__all__ = [
    "clc_server",
    "clc_group",
    "clc_public_ip",
    "clc_load_balancer",
    "clc_load_balancer_pool",
]
