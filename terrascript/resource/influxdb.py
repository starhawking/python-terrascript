# terrascript/resource/influxdb.py
import terrascript


class influxdb_database(terrascript.Resource):
    pass


class influxdb_user(terrascript.Resource):
    pass


class influxdb_continuous_query(terrascript.Resource):
    pass


__all__ = [
    "influxdb_database",
    "influxdb_user",
    "influxdb_continuous_query",
]
