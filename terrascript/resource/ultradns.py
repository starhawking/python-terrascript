# terrascript/resource/ultradns.py
import terrascript


class ultradns_dirpool(terrascript.Resource):
    pass


class ultradns_probe_http(terrascript.Resource):
    pass


class ultradns_probe_ping(terrascript.Resource):
    pass


class ultradns_record(terrascript.Resource):
    pass


class ultradns_tcpool(terrascript.Resource):
    pass


class ultradns_rdpool(terrascript.Resource):
    pass


__all__ = [
    "ultradns_dirpool",
    "ultradns_probe_http",
    "ultradns_probe_ping",
    "ultradns_record",
    "ultradns_tcpool",
    "ultradns_rdpool",
]
