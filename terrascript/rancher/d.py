from terrascript import Data
class rancher_certificate(Data):
    def __init__(self, _label, **kwargs): super().__init__('rancher_certificate', _label, **kwargs)
certificate = rancher_certificate

class rancher_environment(Data):
    def __init__(self, _label, **kwargs): super().__init__('rancher_environment', _label, **kwargs)
environment = rancher_environment

class rancher_setting(Data):
    def __init__(self, _label, **kwargs): super().__init__('rancher_setting', _label, **kwargs)
setting = rancher_setting

