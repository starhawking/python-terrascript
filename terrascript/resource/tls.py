# terrascript/resource/tls.py
import terrascript


class tls_cert_request(terrascript.Resource):
    pass


class tls_locally_signed_cert(terrascript.Resource):
    pass


class tls_private_key(terrascript.Resource):
    pass


class tls_self_signed_cert(terrascript.Resource):
    pass

__all__ = [
    "tls_cert_request",
    "tls_locally_signed_cert",
    "tls_private_key",
    "tls_self_signed_cert",
]
