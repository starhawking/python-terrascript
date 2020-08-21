# terrascript/resource/postgresql.py
import terrascript


class postgresql_database(terrascript.Resource):
    pass


class postgresql_default_privileges(terrascript.Resource):
    pass


class postgresql_extension(terrascript.Resource):
    pass


class postgresql_grant(terrascript.Resource):
    pass


class postgresql_schema(terrascript.Resource):
    pass


class postgresql_role(terrascript.Resource):
    pass


__all__ = [
    "postgresql_database",
    "postgresql_default_privileges",
    "postgresql_extension",
    "postgresql_grant",
    "postgresql_schema",
    "postgresql_role",
]
