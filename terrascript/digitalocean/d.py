from terrascript import Data
class digitalocean_certificate(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_certificate', _label, **kwargs)
certificate = digitalocean_certificate

class digitalocean_database_cluster(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_database_cluster', _label, **kwargs)
database_cluster = digitalocean_database_cluster

class digitalocean_domain(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_domain', _label, **kwargs)
domain = digitalocean_domain

class digitalocean_droplet(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_droplet', _label, **kwargs)
droplet = digitalocean_droplet

class digitalocean_droplet_snapshot(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_droplet_snapshot', _label, **kwargs)
droplet_snapshot = digitalocean_droplet_snapshot

class digitalocean_floating_ip(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_floating_ip', _label, **kwargs)
floating_ip = digitalocean_floating_ip

class digitalocean_image(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_image', _label, **kwargs)
image = digitalocean_image

class digitalocean_kubernetes_cluster(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_kubernetes_cluster', _label, **kwargs)
kubernetes_cluster = digitalocean_kubernetes_cluster

class digitalocean_loadbalancer(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_loadbalancer', _label, **kwargs)
loadbalancer = digitalocean_loadbalancer

class digitalocean_record(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_record', _label, **kwargs)
record = digitalocean_record

class digitalocean_ssh_key(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_ssh_key', _label, **kwargs)
ssh_key = digitalocean_ssh_key

class digitalocean_tag(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_tag', _label, **kwargs)
tag = digitalocean_tag

class digitalocean_volume_snapshot(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_volume_snapshot', _label, **kwargs)
volume_snapshot = digitalocean_volume_snapshot

class digitalocean_volume(Data):
    def __init__(self, _label, **kwargs): super().__init__('digitalocean_volume', _label, **kwargs)
volume = digitalocean_volume

