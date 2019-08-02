from terrascript import Resource
class dyn_record(Resource):
    def __init__(self, _label, **kwargs): super().__init__('dyn_record', _label, **kwargs)
record = dyn_record

