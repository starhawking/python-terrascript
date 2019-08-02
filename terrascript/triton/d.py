from terrascript import Data
class triton_account(Data):
    def __init__(self, _label, **kwargs): super().__init__('triton_account', _label, **kwargs)
account = triton_account

class triton_datacenter(Data):
    def __init__(self, _label, **kwargs): super().__init__('triton_datacenter', _label, **kwargs)
datacenter = triton_datacenter

class triton_image(Data):
    def __init__(self, _label, **kwargs): super().__init__('triton_image', _label, **kwargs)
image = triton_image

class triton_network(Data):
    def __init__(self, _label, **kwargs): super().__init__('triton_network', _label, **kwargs)
network = triton_network

class triton_package(Data):
    def __init__(self, _label, **kwargs): super().__init__('triton_package', _label, **kwargs)
package = triton_package

class triton_fabric_vlan(Data):
    def __init__(self, _label, **kwargs): super().__init__('triton_fabric_vlan', _label, **kwargs)
fabric_vlan = triton_fabric_vlan

class triton_fabric_network(Data):
    def __init__(self, _label, **kwargs): super().__init__('triton_fabric_network', _label, **kwargs)
fabric_network = triton_fabric_network

