from terrascript import Data
class vcd_org(Data):
    def __init__(self, _label, **kwargs): super().__init__('vcd_org', _label, **kwargs)
org = vcd_org

class vcd_lb_service_monitor(Data):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_service_monitor', _label, **kwargs)
lb_service_monitor = vcd_lb_service_monitor

class vcd_lb_server_pool(Data):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_server_pool', _label, **kwargs)
lb_server_pool = vcd_lb_server_pool

class vcd_lb_app_profile(Data):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_app_profile', _label, **kwargs)
lb_app_profile = vcd_lb_app_profile

class vcd_lb_app_rule(Data):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_app_rule', _label, **kwargs)
lb_app_rule = vcd_lb_app_rule

class vcd_lb_virtual_server(Data):
    def __init__(self, _label, **kwargs): super().__init__('vcd_lb_virtual_server', _label, **kwargs)
lb_virtual_server = vcd_lb_virtual_server

