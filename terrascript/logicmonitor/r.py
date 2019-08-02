from terrascript import Resource
class logicmonitor_collector(Resource):
    def __init__(self, _label, **kwargs): super().__init__('logicmonitor_collector', _label, **kwargs)
collector = logicmonitor_collector

class logicmonitor_collector_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('logicmonitor_collector_group', _label, **kwargs)
collector_group = logicmonitor_collector_group

class logicmonitor_device(Resource):
    def __init__(self, _label, **kwargs): super().__init__('logicmonitor_device', _label, **kwargs)
device = logicmonitor_device

class logicmonitor_device_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('logicmonitor_device_group', _label, **kwargs)
device_group = logicmonitor_device_group

