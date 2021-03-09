# terrascript/resource/esxi.py
import terrascript


class esxi_guest(terrascript.Resource):
    pass


class esxi_resource_pool(terrascript.Resource):
    pass


class esxi_virtual_disk(terrascript.Resource):
    pass


class esxi_vswitch(terrascript.Resource):
    pass


class esxi_portgroup(terrascript.Resource):
    pass


__all__ = [
    "esxi_guest",
    "esxi_resource_pool",
    "esxi_virtual_disk",
    "esxi_vswitch",
    "esxi_portgroup",
]
