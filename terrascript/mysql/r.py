from terrascript import Resource
class mysql_database(Resource):
    def __init__(self, _label, **kwargs): super().__init__('mysql_database', _label, **kwargs)
database = mysql_database

class mysql_grant(Resource):
    def __init__(self, _label, **kwargs): super().__init__('mysql_grant', _label, **kwargs)
grant = mysql_grant

class mysql_role(Resource):
    def __init__(self, _label, **kwargs): super().__init__('mysql_role', _label, **kwargs)
role = mysql_role

class mysql_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('mysql_user', _label, **kwargs)
user = mysql_user

class mysql_user_password(Resource):
    def __init__(self, _label, **kwargs): super().__init__('mysql_user_password', _label, **kwargs)
user_password = mysql_user_password

