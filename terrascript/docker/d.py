from terrascript import Data
class docker_registry_image(Data):
    def __init__(self, _label, **kwargs): super().__init__('docker_registry_image', _label, **kwargs)
registry_image = docker_registry_image

class docker_network(Data):
    def __init__(self, _label, **kwargs): super().__init__('docker_network', _label, **kwargs)
network = docker_network

