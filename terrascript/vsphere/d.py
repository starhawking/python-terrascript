from terrascript import Data
class vsphere_compute_cluster(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_compute_cluster', _label, **kwargs)
compute_cluster = vsphere_compute_cluster

class vsphere_custom_attribute(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_custom_attribute', _label, **kwargs)
custom_attribute = vsphere_custom_attribute

class vsphere_datacenter(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_datacenter', _label, **kwargs)
datacenter = vsphere_datacenter

class vsphere_datastore(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_datastore', _label, **kwargs)
datastore = vsphere_datastore

class vsphere_datastore_cluster(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_datastore_cluster', _label, **kwargs)
datastore_cluster = vsphere_datastore_cluster

class vsphere_distributed_virtual_switch(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_distributed_virtual_switch', _label, **kwargs)
distributed_virtual_switch = vsphere_distributed_virtual_switch

class vsphere_folder(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_folder', _label, **kwargs)
folder = vsphere_folder

class vsphere_host(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_host', _label, **kwargs)
host = vsphere_host

class vsphere_network(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_network', _label, **kwargs)
network = vsphere_network

class vsphere_resource_pool(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_resource_pool', _label, **kwargs)
resource_pool = vsphere_resource_pool

class vsphere_tag(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_tag', _label, **kwargs)
tag = vsphere_tag

class vsphere_tag_category(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_tag_category', _label, **kwargs)
tag_category = vsphere_tag_category

class vsphere_vapp_container(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_vapp_container', _label, **kwargs)
vapp_container = vsphere_vapp_container

class vsphere_virtual_machine(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_virtual_machine', _label, **kwargs)
virtual_machine = vsphere_virtual_machine

class vsphere_vmfs_disks(Data):
    def __init__(self, _label, **kwargs): super().__init__('vsphere_vmfs_disks', _label, **kwargs)
vmfs_disks = vsphere_vmfs_disks

