from terrascript import Data
class scaleway_bootscript(Data):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_bootscript', _label, **kwargs)
bootscript = scaleway_bootscript

class scaleway_image(Data):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_image', _label, **kwargs)
image = scaleway_image

class scaleway_security_group(Data):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_security_group', _label, **kwargs)
security_group = scaleway_security_group

class scaleway_volume(Data):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_volume', _label, **kwargs)
volume = scaleway_volume

