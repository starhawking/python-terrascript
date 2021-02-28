# terrascript/grafana/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class grafana_alert_notification(terrascript.Resource):
    pass


class grafana_dashboard(terrascript.Resource):
    pass


class grafana_data_source(terrascript.Resource):
    pass


class grafana_folder(terrascript.Resource):
    pass


class grafana_organization(terrascript.Resource):
    pass
