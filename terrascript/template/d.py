# terrascript/template/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class template_cloudinit_config(terrascript.Data):
    pass


class template_file(terrascript.Data):
    pass
