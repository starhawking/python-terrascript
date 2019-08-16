from terrascript import Data
class kubernetes_secret(Data):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_secret', _label, **kwargs)
secret = kubernetes_secret

class kubernetes_service(Data):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_service', _label, **kwargs)
service = kubernetes_service

class kubernetes_storage_class(Data):
    def __init__(self, _label, **kwargs): super().__init__('kubernetes_storage_class', _label, **kwargs)
storage_class = kubernetes_storage_class

