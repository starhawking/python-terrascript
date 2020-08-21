# terrascript/resource/circonus.py
import terrascript


class circonus_check(terrascript.Resource):
    pass


class circonus_contact_group(terrascript.Resource):
    pass


class circonus_graph(terrascript.Resource):
    pass


class circonus_overlay_set(terrascript.Resource):
    pass


class circonus_dashboard(terrascript.Resource):
    pass


class circonus_maintenance(terrascript.Resource):
    pass


class circonus_metric(terrascript.Resource):
    pass


class circonus_rule_set(terrascript.Resource):
    pass


class circonus_rule_set_group(terrascript.Resource):
    pass


class circonus_worksheet(terrascript.Resource):
    pass


__all__ = [
    "circonus_check",
    "circonus_contact_group",
    "circonus_graph",
    "circonus_overlay_set",
    "circonus_dashboard",
    "circonus_maintenance",
    "circonus_metric",
    "circonus_rule_set",
    "circonus_rule_set_group",
    "circonus_worksheet",
]
