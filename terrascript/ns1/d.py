# terrascript/ns1/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class ns1_dnssec(terrascript.Data):
    pass


class ns1_record(terrascript.Data):
    pass


class ns1_zone(terrascript.Data):
    pass
