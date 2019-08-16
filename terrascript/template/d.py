from terrascript import Data
class template_file(Data):
    def __init__(self, _label, **kwargs): super().__init__('template_file', _label, **kwargs)
file = template_file

class template_cloudinit_config(Data):
    def __init__(self, _label, **kwargs): super().__init__('template_cloudinit_config', _label, **kwargs)
cloudinit_config = template_cloudinit_config

