# terrascript/resource/time.py
import terrascript


class time_offset(terrascript.Resource):
    pass


class time_rotating(terrascript.Resource):
    pass


class time_sleep(terrascript.Resource):
    pass


class time_static(terrascript.Resource):
    pass    


__all__ = [
    "time_offset",
    "time_rotating",
    "time_sleep",
    "time_static",
]
