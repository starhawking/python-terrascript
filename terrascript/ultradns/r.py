from terrascript import Resource
class ultradns_dirpool(Resource):
    def __init__(self, _label, **kwargs): super().__init__('ultradns_dirpool', _label, **kwargs)
dirpool = ultradns_dirpool

class ultradns_probe_http(Resource):
    def __init__(self, _label, **kwargs): super().__init__('ultradns_probe_http', _label, **kwargs)
probe_http = ultradns_probe_http

class ultradns_probe_ping(Resource):
    def __init__(self, _label, **kwargs): super().__init__('ultradns_probe_ping', _label, **kwargs)
probe_ping = ultradns_probe_ping

class ultradns_record(Resource):
    def __init__(self, _label, **kwargs): super().__init__('ultradns_record', _label, **kwargs)
record = ultradns_record

class ultradns_tcpool(Resource):
    def __init__(self, _label, **kwargs): super().__init__('ultradns_tcpool', _label, **kwargs)
tcpool = ultradns_tcpool

class ultradns_rdpool(Resource):
    def __init__(self, _label, **kwargs): super().__init__('ultradns_rdpool', _label, **kwargs)
rdpool = ultradns_rdpool

