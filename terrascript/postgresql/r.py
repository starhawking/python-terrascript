# terrascript/postgresql/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class postgresql_database(terrascript.Resource):
    pass


class postgresql_default_privileges(terrascript.Resource):
    pass


class postgresql_extension(terrascript.Resource):
    pass


class postgresql_grant(terrascript.Resource):
    pass


class postgresql_grant_role(terrascript.Resource):
    pass


class postgresql_role(terrascript.Resource):
    pass


class postgresql_schema(terrascript.Resource):
    pass
