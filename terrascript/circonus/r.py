from terrascript import Resource
class circonus_check(Resource):
    def __init__(self, _label, **kwargs): super().__init__('circonus_check', _label, **kwargs)
check = circonus_check

class circonus_contact_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('circonus_contact_group', _label, **kwargs)
contact_group = circonus_contact_group

class circonus_graph(Resource):
    def __init__(self, _label, **kwargs): super().__init__('circonus_graph', _label, **kwargs)
graph = circonus_graph

class circonus_metric(Resource):
    def __init__(self, _label, **kwargs): super().__init__('circonus_metric', _label, **kwargs)
metric = circonus_metric

class circonus_metric_cluster(Resource):
    def __init__(self, _label, **kwargs): super().__init__('circonus_metric_cluster', _label, **kwargs)
metric_cluster = circonus_metric_cluster

class circonus_rule_set(Resource):
    def __init__(self, _label, **kwargs): super().__init__('circonus_rule_set', _label, **kwargs)
rule_set = circonus_rule_set

class circonus_worksheet(Resource):
    def __init__(self, _label, **kwargs): super().__init__('circonus_worksheet', _label, **kwargs)
worksheet = circonus_worksheet

