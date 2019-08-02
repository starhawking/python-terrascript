from terrascript import Resource
class rancher_certificate(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rancher_certificate', _label, **kwargs)
certificate = rancher_certificate

class rancher_environment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rancher_environment', _label, **kwargs)
environment = rancher_environment

class rancher_host(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rancher_host', _label, **kwargs)
host = rancher_host

class rancher_registration_token(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rancher_registration_token', _label, **kwargs)
registration_token = rancher_registration_token

class rancher_registry(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rancher_registry', _label, **kwargs)
registry = rancher_registry

class rancher_registry_credential(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rancher_registry_credential', _label, **kwargs)
registry_credential = rancher_registry_credential

class rancher_secret(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rancher_secret', _label, **kwargs)
secret = rancher_secret

class rancher_stack(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rancher_stack', _label, **kwargs)
stack = rancher_stack

class rancher_volume(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rancher_volume', _label, **kwargs)
volume = rancher_volume

