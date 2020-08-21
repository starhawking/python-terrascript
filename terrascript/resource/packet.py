# terrascript/resource/packet.py
import terrascript


class packet_device(terrascript.Resource):
    pass


class packet_device_network_type(terrascript.Resource):
    pass


class packet_ssh_key(terrascript.Resource):
    pass


class packet_project_ssh_key(terrascript.Resource):
    pass


class packet_project(terrascript.Resource):
    pass


class packet_organization(terrascript.Resource):
    pass


class packet_volume(terrascript.Resource):
    pass


class packet_volume_attachment(terrascript.Resource):
    pass


class packet_reserved_ip_block(terrascript.Resource):
    pass


class packet_ip_attachment(terrascript.Resource):
    pass


class packet_spot_market_request(terrascript.Resource):
    pass


class packet_vlan(terrascript.Resource):
    pass


class packet_bgp_session(terrascript.Resource):
    pass


class packet_port_vlan_attachment(terrascript.Resource):
    pass


__all__ = [
    "packet_device",
    "packet_device_network_type",
    "packet_ssh_key",
    "packet_project_ssh_key",
    "packet_project",
    "packet_organization",
    "packet_volume",
    "packet_volume_attachment",
    "packet_reserved_ip_block",
    "packet_ip_attachment",
    "packet_spot_market_request",
    "packet_vlan",
    "packet_bgp_session",
    "packet_port_vlan_attachment",
]
