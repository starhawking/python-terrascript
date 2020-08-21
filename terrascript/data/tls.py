# terrascript/data/tls.py
import terrascript


class tls_public_key(terrascript.Data):
    pass


class tls_certificate(terrascript.Data):
    pass


__all__ = [
    "tls_public_key",
    "tls_certificate",
]
