from terrascript import Resource
class cobbler_distro(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cobbler_distro', _label, **kwargs)
distro = cobbler_distro

class cobbler_kickstart_file(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cobbler_kickstart_file', _label, **kwargs)
kickstart_file = cobbler_kickstart_file

class cobbler_profile(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cobbler_profile', _label, **kwargs)
profile = cobbler_profile

class cobbler_repo(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cobbler_repo', _label, **kwargs)
repo = cobbler_repo

class cobbler_snippet(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cobbler_snippet', _label, **kwargs)
snippet = cobbler_snippet

class cobbler_system(Resource):
    def __init__(self, _label, **kwargs): super().__init__('cobbler_system', _label, **kwargs)
system = cobbler_system

