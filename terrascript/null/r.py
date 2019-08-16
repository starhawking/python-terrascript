from terrascript import Resource
class null_resource(Resource):
    def __init__(self, _label, **kwargs): super().__init__('null_resource', _label, **kwargs)
resource = null_resource

