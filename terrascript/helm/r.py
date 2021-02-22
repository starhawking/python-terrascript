# terrascript/helm/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class helm_release(terrascript.Resource):
    pass
