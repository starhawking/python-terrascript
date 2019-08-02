from terrascript import Resource
class docker_container(Resource):
    def __init__(self, _label, **kwargs): super().__init__('docker_container', _label, **kwargs)
container = docker_container

class docker_image(Resource):
    def __init__(self, _label, **kwargs): super().__init__('docker_image', _label, **kwargs)
image = docker_image

class docker_network(Resource):
    def __init__(self, _label, **kwargs): super().__init__('docker_network', _label, **kwargs)
network = docker_network

class docker_volume(Resource):
    def __init__(self, _label, **kwargs): super().__init__('docker_volume', _label, **kwargs)
volume = docker_volume

class docker_config(Resource):
    def __init__(self, _label, **kwargs): super().__init__('docker_config', _label, **kwargs)
config = docker_config

class docker_secret(Resource):
    def __init__(self, _label, **kwargs): super().__init__('docker_secret', _label, **kwargs)
secret = docker_secret

class docker_service(Resource):
    def __init__(self, _label, **kwargs): super().__init__('docker_service', _label, **kwargs)
service = docker_service

