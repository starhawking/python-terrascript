# terrascript/scaleway/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class scaleway_account_ssh_key(terrascript.Resource):
    pass


class scaleway_baremetal_server(terrascript.Resource):
    pass


class scaleway_instance_ip(terrascript.Resource):
    pass


class scaleway_instance_ip_reverse_dns(terrascript.Resource):
    pass


class scaleway_instance_placement_group(terrascript.Resource):
    pass


class scaleway_instance_private_nic(terrascript.Resource):
    pass


class scaleway_instance_security_group(terrascript.Resource):
    pass


class scaleway_instance_security_group_rules(terrascript.Resource):
    pass


class scaleway_instance_server(terrascript.Resource):
    pass


class scaleway_instance_volume(terrascript.Resource):
    pass


class scaleway_k8s_cluster(terrascript.Resource):
    pass


class scaleway_k8s_pool(terrascript.Resource):
    pass


class scaleway_lb(terrascript.Resource):
    pass


class scaleway_lb_backend(terrascript.Resource):
    pass


class scaleway_lb_certificate(terrascript.Resource):
    pass


class scaleway_lb_frontend(terrascript.Resource):
    pass


class scaleway_lb_ip(terrascript.Resource):
    pass


class scaleway_object_bucket(terrascript.Resource):
    pass


class scaleway_rdb_instance(terrascript.Resource):
    pass


class scaleway_rdb_user(terrascript.Resource):
    pass


class scaleway_registry_namespace(terrascript.Resource):
    pass


class scaleway_vpc_private_network(terrascript.Resource):
    pass
