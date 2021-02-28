# terrascript/dnsimple/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class dnsimple_email_forward(terrascript.Resource):
    pass


class dnsimple_record(terrascript.Resource):
    pass
