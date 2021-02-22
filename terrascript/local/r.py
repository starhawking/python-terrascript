# terrascript/local/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class local_file(terrascript.Resource):
    pass
