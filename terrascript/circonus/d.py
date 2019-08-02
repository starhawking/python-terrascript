from terrascript import Data
class circonus_account(Data):
    def __init__(self, _label, **kwargs): super().__init__('circonus_account', _label, **kwargs)
account = circonus_account

class circonus_collector(Data):
    def __init__(self, _label, **kwargs): super().__init__('circonus_collector', _label, **kwargs)
collector = circonus_collector

