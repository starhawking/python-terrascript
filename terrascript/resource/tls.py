# terrascript/resource/tls.py
import terrascript


class tls_private_key(terrascript.Resource):
    pass


class tls_locally_signed_cert(terrascript.Resource):
    pass


class tls_self_signed_cert(terrascript.Resource):
    pass


class tls_cert_request(terrascript.Resource):
    pass


__all__ = [
    "tls_private_key",
    "tls_locally_signed_cert",
    "tls_self_signed_cert",
    "tls_cert_request",
]
