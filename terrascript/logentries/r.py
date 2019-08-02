from terrascript import Resource
class logentries_log(Resource):
    def __init__(self, _label, **kwargs): super().__init__('logentries_log', _label, **kwargs)
log = logentries_log

class logentries_logset(Resource):
    def __init__(self, _label, **kwargs): super().__init__('logentries_logset', _label, **kwargs)
logset = logentries_logset

