from terrascript import Resource
class ns1_zone(Resource):
    def __init__(self, _label, **kwargs): super().__init__('ns1_zone', _label, **kwargs)
zone = ns1_zone

