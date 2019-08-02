from terrascript import Data
class ignition_config(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_config', _label, **kwargs)
config = ignition_config

class ignition_disk(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_disk', _label, **kwargs)
disk = ignition_disk

class ignition_raid(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_raid', _label, **kwargs)
raid = ignition_raid

class ignition_filesystem(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_filesystem', _label, **kwargs)
filesystem = ignition_filesystem

class ignition_file(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_file', _label, **kwargs)
file = ignition_file

class ignition_directory(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_directory', _label, **kwargs)
directory = ignition_directory

class ignition_link(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_link', _label, **kwargs)
link = ignition_link

class ignition_systemd_unit(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_systemd_unit', _label, **kwargs)
systemd_unit = ignition_systemd_unit

class ignition_networkd_unit(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_networkd_unit', _label, **kwargs)
networkd_unit = ignition_networkd_unit

class ignition_user(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_user', _label, **kwargs)
user = ignition_user

class ignition_group(Data):
    def __init__(self, _label, **kwargs): super().__init__('ignition_group', _label, **kwargs)
group = ignition_group

