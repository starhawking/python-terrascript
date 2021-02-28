# terrascript/pagerduty/__init__.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)

import terrascript

class pagerduty(terrascript.Provider):
    pass
