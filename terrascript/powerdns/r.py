from terrascript import Resource
class powerdns_zone(Resource):
    def __init__(self, _label, **kwargs): super().__init__('powerdns_zone', _label, **kwargs)
zone = powerdns_zone

class powerdns_record(Resource):
    def __init__(self, _label, **kwargs): super().__init__('powerdns_record', _label, **kwargs)
record = powerdns_record

