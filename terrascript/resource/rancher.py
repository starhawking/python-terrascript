# terrascript/resource/rancher.py
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


__all__ = [
    "rancher_certificate",
    "rancher_environment",
    "rancher_host",
    "rancher_registration_token",
    "rancher_registry",
    "rancher_registry_credential",
    "rancher_secret",
    "rancher_stack",
    "rancher_volume",
]
