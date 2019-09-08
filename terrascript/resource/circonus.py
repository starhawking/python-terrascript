# terrascript/resource/circonus.py

import terrascript


class circonus_check(terrascript.Resource):
    pass

class circonus_contact_group(terrascript.Resource):
    pass

class circonus_graph(terrascript.Resource):
    pass

class circonus_metric(terrascript.Resource):
    pass

class circonus_metric_cluster(terrascript.Resource):
    pass

class circonus_rule_set(terrascript.Resource):
    pass

class circonus_worksheet(terrascript.Resource):
    pass


__all__ = [
    'circonus_check',
    'circonus_contact_group',
    'circonus_graph',
    'circonus_metric',
    'circonus_metric_cluster',
    'circonus_rule_set',
    'circonus_worksheet',
]