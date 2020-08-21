# terrascript/data/packet.py
import terrascript


class packet_ip_block_ranges(terrascript.Data):
    pass


class packet_precreated_ip_block(terrascript.Data):
    pass


class packet_operating_system(terrascript.Data):
    pass


class packet_organization(terrascript.Data):
    pass


class packet_spot_market_price(terrascript.Data):
    pass


class packet_device(terrascript.Data):
    pass


class packet_device_bgp_neighbors(terrascript.Data):
    pass


class packet_project(terrascript.Data):
    pass


class packet_spot_market_request(terrascript.Data):
    pass


class packet_volume(terrascript.Data):
    pass


__all__ = [
    "packet_ip_block_ranges",
    "packet_precreated_ip_block",
    "packet_operating_system",
    "packet_organization",
    "packet_spot_market_price",
    "packet_device",
    "packet_device_bgp_neighbors",
    "packet_project",
    "packet_spot_market_request",
    "packet_volume",
]
