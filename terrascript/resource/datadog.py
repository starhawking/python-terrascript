# terrascript/resource/datadog.py

import terrascript


class datadog_downtime(terrascript.Resource):
    pass

class datadog_metric_metadata(terrascript.Resource):
    pass

class datadog_monitor(terrascript.Resource):
    pass

class datadog_synthetics_test(terrascript.Resource):
    pass

class datadog_timeboard(terrascript.Resource):
    pass

class datadog_screenboard(terrascript.Resource):
    pass

class datadog_dashboard(terrascript.Resource):
    pass

class datadog_user(terrascript.Resource):
    pass

class datadog_integration_gcp(terrascript.Resource):
    pass

class datadog_integration_aws(terrascript.Resource):
    pass

class datadog_integration_pagerduty(terrascript.Resource):
    pass

class datadog_integration_pagerduty_service_object(terrascript.Resource):
    pass

class datadog_service_level_objective(terrascript.Resource):
    pass


__all__ = [
    'datadog_downtime',
    'datadog_metric_metadata',
    'datadog_monitor',
    'datadog_synthetics_test',
    'datadog_timeboard',
    'datadog_screenboard',
    'datadog_dashboard',
    'datadog_user',
    'datadog_integration_gcp',
    'datadog_integration_aws',
    'datadog_integration_pagerduty',
    'datadog_integration_pagerduty_service_object',
    'datadog_service_level_objective',
]