from terrascript import Data
class pagerduty_escalation_policy(Data):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_escalation_policy', _label, **kwargs)
escalation_policy = pagerduty_escalation_policy

class pagerduty_schedule(Data):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_schedule', _label, **kwargs)
schedule = pagerduty_schedule

class pagerduty_user(Data):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_user', _label, **kwargs)
user = pagerduty_user

class pagerduty_team(Data):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_team', _label, **kwargs)
team = pagerduty_team

class pagerduty_vendor(Data):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_vendor', _label, **kwargs)
vendor = pagerduty_vendor

class pagerduty_extension_schema(Data):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_extension_schema', _label, **kwargs)
extension_schema = pagerduty_extension_schema

class pagerduty_service(Data):
    def __init__(self, _label, **kwargs): super().__init__('pagerduty_service', _label, **kwargs)
service = pagerduty_service

