from terrascript import Data
class null_data_source(Data):
    def __init__(self, _label, **kwargs): super().__init__('null_data_source', _label, **kwargs)
data_source = null_data_source

