# terrascript/pingdom/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class pingdom_check(terrascript.Resource):
    pass


class pingdom_contact(terrascript.Resource):
    pass


class pingdom_team(terrascript.Resource):
    pass


class pingdom_user(terrascript.Resource):
    pass
