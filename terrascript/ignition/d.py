#  terrascript/ignition/d.py

import terrascript


class config(terrascript.Datasource):
    pass

class disk(terrascript.Datasource):
    pass

class raid(terrascript.Datasource):
    pass

class filesystem(terrascript.Datasource):
    pass

class file(terrascript.Datasource):
    pass

class directory(terrascript.Datasource):
    pass

class link(terrascript.Datasource):
    pass

class systemd_unit(terrascript.Datasource):
    pass

class networkd_unit(terrascript.Datasource):
    pass

class user(terrascript.Datasource):
    pass

class group(terrascript.Datasource):
    pass
