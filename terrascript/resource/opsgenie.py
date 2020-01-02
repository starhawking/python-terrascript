# terrascript/resource/opsgenie.py

import terrascript


class opsgenie_team(terrascript.Resource):
    pass

class opsgenie_team_routing_rule(terrascript.Resource):
    pass

class opsgenie_user(terrascript.Resource):
    pass

class opsgenie_user_contact(terrascript.Resource):
    pass

class opsgenie_escalation(terrascript.Resource):
    pass

class opsgenie_api_integration(terrascript.Resource):
    pass

class opsgenie_email_integration(terrascript.Resource):
    pass

class opsgenie_schedule(terrascript.Resource):
    pass

class opsgenie_schedule_rotation(terrascript.Resource):
    pass

class opsgenie_maintenance(terrascript.Resource):
    pass

class opsgenie_heartbeat(terrascript.Resource):
    pass


__all__ = [
    'opsgenie_team',
    'opsgenie_team_routing_rule',
    'opsgenie_user',
    'opsgenie_user_contact',
    'opsgenie_escalation',
    'opsgenie_api_integration',
    'opsgenie_email_integration',
    'opsgenie_schedule',
    'opsgenie_schedule_rotation',
    'opsgenie_maintenance',
    'opsgenie_heartbeat',
]