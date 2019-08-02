from terrascript import Resource
class digitalocean_certificate(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_certificate', _label, **kwargs)
certificate = digitalocean_certificate

class digitalocean_cdn(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_cdn', _label, **kwargs)
cdn = digitalocean_cdn

class digitalocean_database_cluster(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_database_cluster', _label, **kwargs)
database_cluster = digitalocean_database_cluster

class digitalocean_domain(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_domain', _label, **kwargs)
domain = digitalocean_domain

class digitalocean_droplet(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_droplet', _label, **kwargs)
droplet = digitalocean_droplet

class digitalocean_droplet_snapshot(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_droplet_snapshot', _label, **kwargs)
droplet_snapshot = digitalocean_droplet_snapshot

class digitalocean_firewall(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_firewall', _label, **kwargs)
firewall = digitalocean_firewall

class digitalocean_floating_ip(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_floating_ip', _label, **kwargs)
floating_ip = digitalocean_floating_ip

class digitalocean_floating_ip_assignment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_floating_ip_assignment', _label, **kwargs)
floating_ip_assignment = digitalocean_floating_ip_assignment

class digitalocean_kubernetes_cluster(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_kubernetes_cluster', _label, **kwargs)
kubernetes_cluster = digitalocean_kubernetes_cluster

class digitalocean_kubernetes_node_pool(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_kubernetes_node_pool', _label, **kwargs)
kubernetes_node_pool = digitalocean_kubernetes_node_pool

class digitalocean_loadbalancer(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_loadbalancer', _label, **kwargs)
loadbalancer = digitalocean_loadbalancer

class digitalocean_project(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_project', _label, **kwargs)
project = digitalocean_project

class digitalocean_record(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_record', _label, **kwargs)
record = digitalocean_record

class digitalocean_spaces_bucket(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_spaces_bucket', _label, **kwargs)
spaces_bucket = digitalocean_spaces_bucket

class digitalocean_ssh_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_ssh_key', _label, **kwargs)
ssh_key = digitalocean_ssh_key

class digitalocean_tag(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_tag', _label, **kwargs)
tag = digitalocean_tag

class digitalocean_volume(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_volume', _label, **kwargs)
volume = digitalocean_volume

class digitalocean_volume_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_volume_attachment', _label, **kwargs)
volume_attachment = digitalocean_volume_attachment

class digitalocean_volume_snapshot(Resource):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_volume_snapshot', _label, **kwargs)
volume_snapshot = digitalocean_volume_snapshot

