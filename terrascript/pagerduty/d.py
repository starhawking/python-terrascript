# terrascript/pagerduty/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class pagerduty_business_service(terrascript.Data):
    pass


class pagerduty_escalation_policy(terrascript.Data):
    pass


class pagerduty_extension_schema(terrascript.Data):
    pass


class pagerduty_priority(terrascript.Data):
    pass


class pagerduty_ruleset(terrascript.Data):
    pass


class pagerduty_schedule(terrascript.Data):
    pass


class pagerduty_service(terrascript.Data):
    pass


class pagerduty_team(terrascript.Data):
    pass


class pagerduty_user(terrascript.Data):
    pass


class pagerduty_user_contact_method(terrascript.Data):
    pass


class pagerduty_vendor(terrascript.Data):
    pass
