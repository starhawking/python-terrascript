from terrascript import Resource
class postgresql_database(Resource):
    def __init__(self, _label, **kwargs): super().__init__('postgresql_database', _label, **kwargs)
database = postgresql_database

class postgresql_default_privileges(Resource):
    def __init__(self, _label, **kwargs): super().__init__('postgresql_default_privileges', _label, **kwargs)
default_privileges = postgresql_default_privileges

class postgresql_extension(Resource):
    def __init__(self, _label, **kwargs): super().__init__('postgresql_extension', _label, **kwargs)
extension = postgresql_extension

class postgresql_grant(Resource):
    def __init__(self, _label, **kwargs): super().__init__('postgresql_grant', _label, **kwargs)
grant = postgresql_grant

class postgresql_schema(Resource):
    def __init__(self, _label, **kwargs): super().__init__('postgresql_schema', _label, **kwargs)
schema = postgresql_schema

class postgresql_role(Resource):
    def __init__(self, _label, **kwargs): super().__init__('postgresql_role', _label, **kwargs)
role = postgresql_role

