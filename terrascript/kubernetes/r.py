from terrascript import Resource
class kubernetes_cluster_role(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_cluster_role', _label, **kwargs)
cluster_role = kubernetes_cluster_role

class kubernetes_cluster_role_binding(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_cluster_role_binding', _label, **kwargs)
cluster_role_binding = kubernetes_cluster_role_binding

class kubernetes_config_map(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_config_map', _label, **kwargs)
config_map = kubernetes_config_map

class kubernetes_cron_job(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_cron_job', _label, **kwargs)
cron_job = kubernetes_cron_job

class kubernetes_daemonset(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_daemonset', _label, **kwargs)
daemonset = kubernetes_daemonset

class kubernetes_deployment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_deployment', _label, **kwargs)
deployment = kubernetes_deployment

class kubernetes_endpoints(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_endpoints', _label, **kwargs)
endpoints = kubernetes_endpoints

class kubernetes_horizontal_pod_autoscaler(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_horizontal_pod_autoscaler', _label, **kwargs)
horizontal_pod_autoscaler = kubernetes_horizontal_pod_autoscaler

class kubernetes_ingress(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_ingress', _label, **kwargs)
ingress = kubernetes_ingress

class kubernetes_job(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_job', _label, **kwargs)
job = kubernetes_job

class kubernetes_limit_range(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_limit_range', _label, **kwargs)
limit_range = kubernetes_limit_range

class kubernetes_namespace(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_namespace', _label, **kwargs)
namespace = kubernetes_namespace

class kubernetes_network_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_network_policy', _label, **kwargs)
network_policy = kubernetes_network_policy

class kubernetes_persistent_volume(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_persistent_volume', _label, **kwargs)
persistent_volume = kubernetes_persistent_volume

class kubernetes_persistent_volume_claim(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_persistent_volume_claim', _label, **kwargs)
persistent_volume_claim = kubernetes_persistent_volume_claim

class kubernetes_pod(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_pod', _label, **kwargs)
pod = kubernetes_pod

class kubernetes_replication_controller(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_replication_controller', _label, **kwargs)
replication_controller = kubernetes_replication_controller

class kubernetes_role_binding(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_role_binding', _label, **kwargs)
role_binding = kubernetes_role_binding

class kubernetes_resource_quota(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_resource_quota', _label, **kwargs)
resource_quota = kubernetes_resource_quota

class kubernetes_role(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_role', _label, **kwargs)
role = kubernetes_role

class kubernetes_secret(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_secret', _label, **kwargs)
secret = kubernetes_secret

class kubernetes_service(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_service', _label, **kwargs)
service = kubernetes_service

class kubernetes_service_account(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_service_account', _label, **kwargs)
service_account = kubernetes_service_account

class kubernetes_stateful_set(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_stateful_set', _label, **kwargs)
stateful_set = kubernetes_stateful_set

class kubernetes_storage_class(Resource):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_storage_class', _label, **kwargs)
storage_class = kubernetes_storage_class

