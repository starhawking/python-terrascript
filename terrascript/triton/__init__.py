# terrascript/triton/__init__.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)

import terrascript

class triton(terrascript.Provider):
    pass
