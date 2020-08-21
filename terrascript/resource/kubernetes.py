# terrascript/resource/kubernetes.py
import terrascript


class kubernetes_api_service(terrascript.Resource):
    pass


class kubernetes_certificate_signing_request(terrascript.Resource):
    pass


class kubernetes_cluster_role(terrascript.Resource):
    pass


class kubernetes_cluster_role_binding(terrascript.Resource):
    pass


class kubernetes_config_map(terrascript.Resource):
    pass


class kubernetes_cron_job(terrascript.Resource):
    pass


class kubernetes_csi_driver(terrascript.Resource):
    pass


class kubernetes_daemonset(terrascript.Resource):
    pass


class kubernetes_deployment(terrascript.Resource):
    pass


class kubernetes_endpoints(terrascript.Resource):
    pass


class kubernetes_horizontal_pod_autoscaler(terrascript.Resource):
    pass


class kubernetes_ingress(terrascript.Resource):
    pass


class kubernetes_job(terrascript.Resource):
    pass


class kubernetes_limit_range(terrascript.Resource):
    pass


class kubernetes_namespace(terrascript.Resource):
    pass


class kubernetes_network_policy(terrascript.Resource):
    pass


class kubernetes_persistent_volume(terrascript.Resource):
    pass


class kubernetes_persistent_volume_claim(terrascript.Resource):
    pass


class kubernetes_pod(terrascript.Resource):
    pass


class kubernetes_pod_disruption_budget(terrascript.Resource):
    pass


class kubernetes_pod_security_policy(terrascript.Resource):
    pass


class kubernetes_priority_class(terrascript.Resource):
    pass


class kubernetes_replication_controller(terrascript.Resource):
    pass


class kubernetes_role_binding(terrascript.Resource):
    pass


class kubernetes_resource_quota(terrascript.Resource):
    pass


class kubernetes_role(terrascript.Resource):
    pass


class kubernetes_secret(terrascript.Resource):
    pass


class kubernetes_service(terrascript.Resource):
    pass


class kubernetes_service_account(terrascript.Resource):
    pass


class kubernetes_stateful_set(terrascript.Resource):
    pass


class kubernetes_storage_class(terrascript.Resource):
    pass


class kubernetes_validating_webhook_configuration(terrascript.Resource):
    pass


class kubernetes_mutating_webhook_configuration(terrascript.Resource):
    pass


__all__ = [
    "kubernetes_api_service",
    "kubernetes_certificate_signing_request",
    "kubernetes_cluster_role",
    "kubernetes_cluster_role_binding",
    "kubernetes_config_map",
    "kubernetes_cron_job",
    "kubernetes_csi_driver",
    "kubernetes_daemonset",
    "kubernetes_deployment",
    "kubernetes_endpoints",
    "kubernetes_horizontal_pod_autoscaler",
    "kubernetes_ingress",
    "kubernetes_job",
    "kubernetes_limit_range",
    "kubernetes_namespace",
    "kubernetes_network_policy",
    "kubernetes_persistent_volume",
    "kubernetes_persistent_volume_claim",
    "kubernetes_pod",
    "kubernetes_pod_disruption_budget",
    "kubernetes_pod_security_policy",
    "kubernetes_priority_class",
    "kubernetes_replication_controller",
    "kubernetes_role_binding",
    "kubernetes_resource_quota",
    "kubernetes_role",
    "kubernetes_secret",
    "kubernetes_service",
    "kubernetes_service_account",
    "kubernetes_stateful_set",
    "kubernetes_storage_class",
    "kubernetes_validating_webhook_configuration",
    "kubernetes_mutating_webhook_configuration",
]
