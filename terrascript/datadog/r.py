from terrascript import Resource
class datadog_downtime(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_downtime', _label, **kwargs)
downtime = datadog_downtime

class datadog_metric_metadata(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_metric_metadata', _label, **kwargs)
metric_metadata = datadog_metric_metadata

class datadog_monitor(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_monitor', _label, **kwargs)
monitor = datadog_monitor

class datadog_synthetics_test(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_synthetics_test', _label, **kwargs)
synthetics_test = datadog_synthetics_test

class datadog_timeboard(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_timeboard', _label, **kwargs)
timeboard = datadog_timeboard

class datadog_screenboard(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_screenboard', _label, **kwargs)
screenboard = datadog_screenboard

class datadog_dashboard(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_dashboard', _label, **kwargs)
dashboard = datadog_dashboard

class datadog_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_user', _label, **kwargs)
user = datadog_user

class datadog_integration_gcp(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_integration_gcp', _label, **kwargs)
integration_gcp = datadog_integration_gcp

class datadog_integration_aws(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_integration_aws', _label, **kwargs)
integration_aws = datadog_integration_aws

class datadog_integration_pagerduty(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_integration_pagerduty', _label, **kwargs)
integration_pagerduty = datadog_integration_pagerduty

class datadog_integration_pagerduty_service_object(Resource):
    def __init__(self, _label, **kwargs): super().__init__('datadog_integration_pagerduty_service_object', _label, **kwargs)
integration_pagerduty_service_object = datadog_integration_pagerduty_service_object

