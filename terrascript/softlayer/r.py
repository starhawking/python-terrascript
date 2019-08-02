from terrascript import Resource
class softlayer_virtual_guest(Resource):
    def __init__(self, _label, **kwargs): super().__init__('softlayer_virtual_guest', _label, **kwargs)
virtual_guest = softlayer_virtual_guest

class softlayer_ssh_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('softlayer_ssh_key', _label, **kwargs)
ssh_key = softlayer_ssh_key

