# terrascript/ns1/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class ns1_apikey(terrascript.Resource):
    pass


class ns1_datafeed(terrascript.Resource):
    pass


class ns1_datasource(terrascript.Resource):
    pass


class ns1_monitoringjob(terrascript.Resource):
    pass


class ns1_notifylist(terrascript.Resource):
    pass


class ns1_record(terrascript.Resource):
    pass


class ns1_team(terrascript.Resource):
    pass


class ns1_user(terrascript.Resource):
    pass


class ns1_zone(terrascript.Resource):
    pass
