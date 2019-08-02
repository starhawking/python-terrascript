from terrascript import Resource
class pagerduty_addon(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_addon', _label, **kwargs)
addon = pagerduty_addon

class pagerduty_escalation_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_escalation_policy', _label, **kwargs)
escalation_policy = pagerduty_escalation_policy

class pagerduty_maintenance_window(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_maintenance_window', _label, **kwargs)
maintenance_window = pagerduty_maintenance_window

class pagerduty_schedule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_schedule', _label, **kwargs)
schedule = pagerduty_schedule

class pagerduty_service(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_service', _label, **kwargs)
service = pagerduty_service

class pagerduty_service_integration(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_service_integration', _label, **kwargs)
service_integration = pagerduty_service_integration

class pagerduty_team(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_team', _label, **kwargs)
team = pagerduty_team

class pagerduty_team_membership(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_team_membership', _label, **kwargs)
team_membership = pagerduty_team_membership

class pagerduty_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_user', _label, **kwargs)
user = pagerduty_user

class pagerduty_user_contact_method(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_user_contact_method', _label, **kwargs)
user_contact_method = pagerduty_user_contact_method

class pagerduty_extension(Resource):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_extension', _label, **kwargs)
extension = pagerduty_extension

