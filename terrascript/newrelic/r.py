from terrascript import Resource
class newrelic_alert_channel(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_alert_channel', _label, **kwargs)
alert_channel = newrelic_alert_channel

class newrelic_alert_condition(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_alert_condition', _label, **kwargs)
alert_condition = newrelic_alert_condition

class newrelic_alert_policy_channel(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_alert_policy_channel', _label, **kwargs)
alert_policy_channel = newrelic_alert_policy_channel

class newrelic_alert_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_alert_policy', _label, **kwargs)
alert_policy = newrelic_alert_policy

class newrelic_dashboard(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_dashboard', _label, **kwargs)
dashboard = newrelic_dashboard

class newrelic_infra_alert_condition(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_infra_alert_condition', _label, **kwargs)
infra_alert_condition = newrelic_infra_alert_condition

class newrelic_nrql_alert_condition(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_nrql_alert_condition', _label, **kwargs)
nrql_alert_condition = newrelic_nrql_alert_condition

class newrelic_synthetics_alert_condition(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_synthetics_alert_condition', _label, **kwargs)
synthetics_alert_condition = newrelic_synthetics_alert_condition

class newrelic_synthetics_monitor(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_synthetics_monitor', _label, **kwargs)
synthetics_monitor = newrelic_synthetics_monitor

class newrelic_synthetics_monitor_script(Resource):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_synthetics_monitor_script', _label, **kwargs)
synthetics_monitor_script = newrelic_synthetics_monitor_script

