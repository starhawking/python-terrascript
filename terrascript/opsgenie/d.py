# terrascript/opsgenie/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class opsgenie_escalation(terrascript.Data):
    pass


class opsgenie_heartbeat(terrascript.Data):
    pass


class opsgenie_schedule(terrascript.Data):
    pass


class opsgenie_service(terrascript.Data):
    pass


class opsgenie_team(terrascript.Data):
    pass


class opsgenie_user(terrascript.Data):
    pass
