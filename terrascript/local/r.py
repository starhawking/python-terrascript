from terrascript import Resource
class local_file(Resource):
    def __init__(self, _label, **kwargs): super().__init__('local_file', _label, **kwargs)
file = local_file

