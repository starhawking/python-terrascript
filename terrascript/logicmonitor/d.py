from terrascript import Data
class logicmonitor_collectors(Data):
    def __init__(self, _label, **kwargs): super().__init__('logicmonitor_collectors', _label, **kwargs)
collectors = logicmonitor_collectors

class logicmonitor_device_group(Data):
    def __init__(self, _label, **kwargs): super().__init__('logicmonitor_device_group', _label, **kwargs)
device_group = logicmonitor_device_group

