# terrascript/resource/librato.py
import terrascript


class librato_space(terrascript.Resource):
    pass


class librato_space_chart(terrascript.Resource):
    pass


class librato_metric(terrascript.Resource):
    pass


class librato_alert(terrascript.Resource):
    pass


class librato_service(terrascript.Resource):
    pass


__all__ = [
    "librato_space",
    "librato_space_chart",
    "librato_metric",
    "librato_alert",
    "librato_service",
]
