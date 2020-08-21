# terrascript/data/newrelic.py
import terrascript


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


class newrelic_synthetics_secure_credential(terrascript.Data):
    pass


__all__ = [
    "newrelic_alert_channel",
    "newrelic_alert_policy",
    "newrelic_application",
    "newrelic_entity",
    "newrelic_key_transaction",
    "newrelic_plugin",
    "newrelic_plugin_component",
    "newrelic_synthetics_monitor",
    "newrelic_synthetics_secure_credential",
]
