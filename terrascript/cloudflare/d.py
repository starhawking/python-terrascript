from terrascript import Data
class cloudflare_ip_ranges(Data):
    def __init__(self, _label, **kwargs): super().__init__('cloudflare_ip_ranges', _label, **kwargs)
ip_ranges = cloudflare_ip_ranges

class cloudflare_zones(Data):
    def __init__(self, _label, **kwargs): super().__init__('cloudflare_zones', _label, **kwargs)
zones = cloudflare_zones

