from terrascript import Data
class profitbricks_datacenter(Data):
    def __init__(self, _label, **kwargs): super().__init__('profitbricks_datacenter', _label, **kwargs)
datacenter = profitbricks_datacenter

class profitbricks_location(Data):
    def __init__(self, _label, **kwargs): super().__init__('profitbricks_location', _label, **kwargs)
location = profitbricks_location

class profitbricks_image(Data):
    def __init__(self, _label, **kwargs): super().__init__('profitbricks_image', _label, **kwargs)
image = profitbricks_image

class profitbricks_resource(Data):
    def __init__(self, _label, **kwargs): super().__init__('profitbricks_resource', _label, **kwargs)
resource = profitbricks_resource

class profitbricks_snapshot(Data):
    def __init__(self, _label, **kwargs): super().__init__('profitbricks_snapshot', _label, **kwargs)
snapshot = profitbricks_snapshot

