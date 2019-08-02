from terrascript import Data
class tls_public_key(Data):
    def __init__(self, _label, **kwargs): super().__init__('tls_public_key', _label, **kwargs)
public_key = tls_public_key

