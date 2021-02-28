# terrascript/ultradns/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class ultradns_dirpool(terrascript.Resource):
    pass


class ultradns_probe_http(terrascript.Resource):
    pass


class ultradns_probe_ping(terrascript.Resource):
    pass


class ultradns_rdpool(terrascript.Resource):
    pass


class ultradns_record(terrascript.Resource):
    pass


class ultradns_tcpool(terrascript.Resource):
    pass
