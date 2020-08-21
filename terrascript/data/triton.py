# terrascript/data/triton.py
import terrascript


class triton_account(terrascript.Data):
    pass


class triton_datacenter(terrascript.Data):
    pass


class triton_image(terrascript.Data):
    pass


class triton_network(terrascript.Data):
    pass


class triton_package(terrascript.Data):
    pass


class triton_fabric_vlan(terrascript.Data):
    pass


class triton_fabric_network(terrascript.Data):
    pass


class triton_volume(terrascript.Data):
    pass


__all__ = [
    "triton_account",
    "triton_datacenter",
    "triton_image",
    "triton_network",
    "triton_package",
    "triton_fabric_vlan",
    "triton_fabric_network",
    "triton_volume",
]
