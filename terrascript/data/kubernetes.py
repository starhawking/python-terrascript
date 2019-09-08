# terrascript/data/kubernetes.py

import terrascript


class kubernetes_secret(terrascript.Data):
    pass

class kubernetes_service(terrascript.Data):
    pass

class kubernetes_storage_class(terrascript.Data):
    pass


__all__ = [
    'kubernetes_secret',
    'kubernetes_service',
    'kubernetes_storage_class',
]