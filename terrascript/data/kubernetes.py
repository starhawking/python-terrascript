# terrascript/data/kubernetes.py
import terrascript


class kubernetes_all_namespaces(terrascript.Data):
    pass


class kubernetes_config_map(terrascript.Data):
    pass


class kubernetes_ingress(terrascript.Data):
    pass


class kubernetes_namespace(terrascript.Data):
    pass


class kubernetes_secret(terrascript.Data):
    pass


class kubernetes_service(terrascript.Data):
    pass


class kubernetes_service_account(terrascript.Data):
    pass


class kubernetes_storage_class(terrascript.Data):
    pass


class kubernetes_pod(terrascript.Data):
    pass


class kubernetes_persistent_volume_claim(terrascript.Data):
    pass


__all__ = [
    "kubernetes_all_namespaces",
    "kubernetes_config_map",
    "kubernetes_ingress",
    "kubernetes_namespace",
    "kubernetes_secret",
    "kubernetes_service",
    "kubernetes_service_account",
    "kubernetes_storage_class",
    "kubernetes_pod",
    "kubernetes_persistent_volume_claim",
]
