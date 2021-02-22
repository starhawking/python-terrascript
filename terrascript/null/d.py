# terrascript/null/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class null_data_source(terrascript.Data):
    pass
