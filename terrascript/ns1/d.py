from terrascript import Data
class ns1_zone(Data):
    def __init__(self, _label, **kwargs): super().__init__('ns1_zone', _label, **kwargs)
zone = ns1_zone

class ns1_datasource(Data):
    def __init__(self, _label, **kwargs): super().__init__('ns1_datasource', _label, **kwargs)
datasource = ns1_datasource

class ns1_datafeed(Data):
    def __init__(self, _label, **kwargs): super().__init__('ns1_datafeed', _label, **kwargs)
datafeed = ns1_datafeed

