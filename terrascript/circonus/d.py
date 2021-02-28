# terrascript/circonus/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class circonus_account(terrascript.Data):
    pass


class circonus_collector(terrascript.Data):
    pass
