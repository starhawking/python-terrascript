from terrascript import Resource
class dnsimple_record(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dnsimple_record', _label, **kwargs)
record = dnsimple_record

