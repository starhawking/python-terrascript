from terrascript import Resource
class tls_private_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('tls_private_key', _label, **kwargs)
private_key = tls_private_key

class tls_locally_signed_cert(Resource):
    def __init__(self, _label, **kwargs): super().__init__('tls_locally_signed_cert', _label, **kwargs)
locally_signed_cert = tls_locally_signed_cert

class tls_self_signed_cert(Resource):
    def __init__(self, _label, **kwargs): super().__init__('tls_self_signed_cert', _label, **kwargs)
self_signed_cert = tls_self_signed_cert

class tls_cert_request(Resource):
    def __init__(self, _label, **kwargs): super().__init__('tls_cert_request', _label, **kwargs)
cert_request = tls_cert_request

