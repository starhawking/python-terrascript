# terrascript/rancher/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class rancher_certificate(terrascript.Resource):
    pass


class rancher_environment(terrascript.Resource):
    pass


class rancher_host(terrascript.Resource):
    pass


class rancher_registration_token(terrascript.Resource):
    pass


class rancher_registry(terrascript.Resource):
    pass


class rancher_registry_credential(terrascript.Resource):
    pass


class rancher_secret(terrascript.Resource):
    pass


class rancher_stack(terrascript.Resource):
    pass


class rancher_volume(terrascript.Resource):
    pass
