# terrascript/resource/newrelic.py

import terrascript


class newrelic_alert_channel(terrascript.Resource):
    pass

class newrelic_alert_condition(terrascript.Resource):
    pass

class newrelic_alert_policy_channel(terrascript.Resource):
    pass

class newrelic_alert_policy(terrascript.Resource):
    pass

class newrelic_plugins_alert_condition(terrascript.Resource):
    pass

class newrelic_dashboard(terrascript.Resource):
    pass

class newrelic_infra_alert_condition(terrascript.Resource):
    pass

class newrelic_insights_event(terrascript.Resource):
    pass

class newrelic_nrql_alert_condition(terrascript.Resource):
    pass

class newrelic_synthetics_alert_condition(terrascript.Resource):
    pass

class newrelic_synthetics_monitor(terrascript.Resource):
    pass

class newrelic_synthetics_monitor_script(terrascript.Resource):
    pass


__all__ = [
    'newrelic_alert_channel',
    'newrelic_alert_condition',
    'newrelic_alert_policy_channel',
    'newrelic_alert_policy',
    'newrelic_plugins_alert_condition',
    'newrelic_dashboard',
    'newrelic_infra_alert_condition',
    'newrelic_insights_event',
    'newrelic_nrql_alert_condition',
    'newrelic_synthetics_alert_condition',
    'newrelic_synthetics_monitor',
    'newrelic_synthetics_monitor_script',
]