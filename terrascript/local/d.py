from terrascript import Data
class local_file(Data):
    def __init__(self, _label, **kwargs): super().__init__('local_file', _label, **kwargs)
file = local_file

