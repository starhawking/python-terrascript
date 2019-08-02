from terrascript import Resource
class dns_a_record_set(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dns_a_record_set', _label, **kwargs)
a_record_set = dns_a_record_set

class dns_aaaa_record_set(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dns_aaaa_record_set', _label, **kwargs)
aaaa_record_set = dns_aaaa_record_set

class dns_cname_record(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dns_cname_record', _label, **kwargs)
cname_record = dns_cname_record

class dns_mx_record_set(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dns_mx_record_set', _label, **kwargs)
mx_record_set = dns_mx_record_set

class dns_ns_record_set(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dns_ns_record_set', _label, **kwargs)
ns_record_set = dns_ns_record_set

class dns_ptr_record(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dns_ptr_record', _label, **kwargs)
ptr_record = dns_ptr_record

class dns_srv_record_set(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dns_srv_record_set', _label, **kwargs)
srv_record_set = dns_srv_record_set

class dns_txt_record_set(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dns_txt_record_set', _label, **kwargs)
txt_record_set = dns_txt_record_set

