# terrascript/resource/mysql.py
import terrascript


class mysql_database(terrascript.Resource):
    pass


class mysql_grant(terrascript.Resource):
    pass


class mysql_role(terrascript.Resource):
    pass


class mysql_user(terrascript.Resource):
    pass


class mysql_user_password(terrascript.Resource):
    pass


__all__ = [
    "mysql_database",
    "mysql_grant",
    "mysql_role",
    "mysql_user",
    "mysql_user_password",
]
