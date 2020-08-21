# terrascript/resource/oneandone.py
import terrascript


class oneandone_server(terrascript.Resource):
    pass


class oneandone_firewall_policy(terrascript.Resource):
    pass


class oneandone_private_network(terrascript.Resource):
    pass


class oneandone_public_ip(terrascript.Resource):
    pass


class oneandone_shared_storage(terrascript.Resource):
    pass


class oneandone_monitoring_policy(terrascript.Resource):
    pass


class oneandone_loadbalancer(terrascript.Resource):
    pass


class oneandone_vpn(terrascript.Resource):
    pass


class oneandone_ssh_key(terrascript.Resource):
    pass


class oneandone_block_storage(terrascript.Resource):
    pass


class oneandone_image(terrascript.Resource):
    pass


class oneandone_baremetal(terrascript.Resource):
    pass


__all__ = [
    "oneandone_server",
    "oneandone_firewall_policy",
    "oneandone_private_network",
    "oneandone_public_ip",
    "oneandone_shared_storage",
    "oneandone_monitoring_policy",
    "oneandone_loadbalancer",
    "oneandone_vpn",
    "oneandone_ssh_key",
    "oneandone_block_storage",
    "oneandone_image",
    "oneandone_baremetal",
]
