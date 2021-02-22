# terrascript/fastly/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class fastly_ip_ranges(terrascript.Data):
    pass


class fastly_waf_rules(terrascript.Data):
    pass
