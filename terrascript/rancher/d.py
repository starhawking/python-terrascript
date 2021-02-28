# terrascript/rancher/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class rancher_certificate(terrascript.Data):
    pass


class rancher_environment(terrascript.Data):
    pass


class rancher_setting(terrascript.Data):
    pass
