# terrascript/data/vcd.py

import terrascript


class vcd_org(terrascript.Data):
    pass

class vcd_catalog(terrascript.Data):
    pass

class vcd_catalog_item(terrascript.Data):
    pass

class vcd_external_network(terrascript.Data):
    pass

class vcd_lb_service_monitor(terrascript.Data):
    pass

class vcd_lb_server_pool(terrascript.Data):
    pass

class vcd_lb_app_profile(terrascript.Data):
    pass

class vcd_lb_app_rule(terrascript.Data):
    pass

class vcd_lb_virtual_server(terrascript.Data):
    pass


__all__ = [
    'vcd_org',
    'vcd_catalog',
    'vcd_catalog_item',
    'vcd_external_network',
    'vcd_lb_service_monitor',
    'vcd_lb_server_pool',
    'vcd_lb_app_profile',
    'vcd_lb_app_rule',
    'vcd_lb_virtual_server',
]