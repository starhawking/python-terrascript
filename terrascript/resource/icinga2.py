# terrascript/resource/icinga2.py
import terrascript


class icinga2_host(terrascript.Resource):
    pass


class icinga2_hostgroup(terrascript.Resource):
    pass


class icinga2_checkcommand(terrascript.Resource):
    pass


class icinga2_service(terrascript.Resource):
    pass


class icinga2_user(terrascript.Resource):
    pass


class icinga2_notification(terrascript.Resource):
    pass


__all__ = [
    "icinga2_host",
    "icinga2_hostgroup",
    "icinga2_checkcommand",
    "icinga2_service",
    "icinga2_user",
    "icinga2_notification",
]
