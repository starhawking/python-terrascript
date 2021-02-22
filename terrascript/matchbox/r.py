# terrascript/matchbox/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class matchbox_group(terrascript.Resource):
    pass


class matchbox_profile(terrascript.Resource):
    pass
