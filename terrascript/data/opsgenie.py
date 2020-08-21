# terrascript/data/opsgenie.py
import terrascript


class opsgenie_team(terrascript.Data):
    pass


class opsgenie_user(terrascript.Data):
    pass


class opsgenie_escalation(terrascript.Data):
    pass


class opsgenie_schedule(terrascript.Data):
    pass


class opsgenie_heartbeat(terrascript.Data):
    pass


class opsgenie_service(terrascript.Data):
    pass


__all__ = [
    "opsgenie_team",
    "opsgenie_user",
    "opsgenie_escalation",
    "opsgenie_schedule",
    "opsgenie_heartbeat",
    "opsgenie_service",
]
