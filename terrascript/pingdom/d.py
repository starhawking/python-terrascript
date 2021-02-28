# terrascript/pingdom/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class pingdom_user(terrascript.Data):
    pass
