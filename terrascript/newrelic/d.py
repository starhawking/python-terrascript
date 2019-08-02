from terrascript import Data
class newrelic_alert_channel(Data):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_alert_channel', _label, **kwargs)
alert_channel = newrelic_alert_channel

class newrelic_alert_policy(Data):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_alert_policy', _label, **kwargs)
alert_policy = newrelic_alert_policy

class newrelic_application(Data):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_application', _label, **kwargs)
application = newrelic_application

class newrelic_key_transaction(Data):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_key_transaction', _label, **kwargs)
key_transaction = newrelic_key_transaction

class newrelic_synthetics_monitor(Data):
    def __init__(self, _label, **kwargs): super().__init__('newrelic_synthetics_monitor', _label, **kwargs)
synthetics_monitor = newrelic_synthetics_monitor

