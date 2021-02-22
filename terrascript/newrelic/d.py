# terrascript/newrelic/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class newrelic_account(terrascript.Data):
    pass


class newrelic_alert_channel(terrascript.Data):
    pass


class newrelic_alert_policy(terrascript.Data):
    pass


class newrelic_application(terrascript.Data):
    pass


class newrelic_entity(terrascript.Data):
    pass


class newrelic_key_transaction(terrascript.Data):
    pass


class newrelic_plugin(terrascript.Data):
    pass


class newrelic_plugin_component(terrascript.Data):
    pass


class newrelic_synthetics_monitor(terrascript.Data):
    pass


class newrelic_synthetics_monitor_location(terrascript.Data):
    pass


class newrelic_synthetics_secure_credential(terrascript.Data):
    pass
