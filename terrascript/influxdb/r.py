from terrascript import Resource
class influxdb_database(Resource):
    def __init__(self, _label, **kwargs): super().__init__('influxdb_database', _label, **kwargs)
database = influxdb_database

class influxdb_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('influxdb_user', _label, **kwargs)
user = influxdb_user

class influxdb_continuous_query(Resource):
    def __init__(self, _label, **kwargs): super().__init__('influxdb_continuous_query', _label, **kwargs)
continuous_query = influxdb_continuous_query

