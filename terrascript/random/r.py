from terrascript import Resource
class random_id(Resource):
    def __init__(self, _label, **kwargs): super().__init__('random_id', _label, **kwargs)
id = random_id

class random_shuffle(Resource):
    def __init__(self, _label, **kwargs): super().__init__('random_shuffle', _label, **kwargs)
shuffle = random_shuffle

class random_pet(Resource):
    def __init__(self, _label, **kwargs): super().__init__('random_pet', _label, **kwargs)
pet = random_pet

class random_string(Resource):
    def __init__(self, _label, **kwargs): super().__init__('random_string', _label, **kwargs)
string = random_string

class random_password(Resource):
    def __init__(self, _label, **kwargs): super().__init__('random_password', _label, **kwargs)
password = random_password

class random_integer(Resource):
    def __init__(self, _label, **kwargs): super().__init__('random_integer', _label, **kwargs)
integer = random_integer

class random_uuid(Resource):
    def __init__(self, _label, **kwargs): super().__init__('random_uuid', _label, **kwargs)
uuid = random_uuid

