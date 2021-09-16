# terrascript/data/time.py
import terrascript


class time_offset(terrascript.Data):
    pass


class time_rotating(terrascript.Data):
    pass


class time_sleep(terrascript.Data):
    pass


class time_static(terrascript.Data):
    pass    


__all__ = [
    "time_offset",
    "time_rotating",
    "time_sleep",
    "time_static",
]
