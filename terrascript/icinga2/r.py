from terrascript import Resource
class icinga2_host(Resource):
    def __init__(self, _label, **kwargs): super().__init__('icinga2_host', _label, **kwargs)
host = icinga2_host

class icinga2_hostgroup(Resource):
    def __init__(self, _label, **kwargs): super().__init__('icinga2_hostgroup', _label, **kwargs)
hostgroup = icinga2_hostgroup

class icinga2_checkcommand(Resource):
    def __init__(self, _label, **kwargs): super().__init__('icinga2_checkcommand', _label, **kwargs)
checkcommand = icinga2_checkcommand

class icinga2_service(Resource):
    def __init__(self, _label, **kwargs): super().__init__('icinga2_service', _label, **kwargs)
service = icinga2_service

class icinga2_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('icinga2_user', _label, **kwargs)
user = icinga2_user

class icinga2_notification(Resource):
    def __init__(self, _label, **kwargs): super().__init__('icinga2_notification', _label, **kwargs)
notification = icinga2_notification

