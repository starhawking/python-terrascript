from terrascript import Resource
class opsgenie_team(Resource):
    def __init__(self, _label, **kwargs): super().__init__('opsgenie_team', _label, **kwargs)
team = opsgenie_team

class opsgenie_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('opsgenie_user', _label, **kwargs)
user = opsgenie_user

