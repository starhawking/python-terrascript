from terrascript import Resource
class azure_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_instance', _label, **kwargs)
instance = azure_instance

class azure_affinity_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_affinity_group', _label, **kwargs)
affinity_group = azure_affinity_group

class azure_data_disk(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_data_disk', _label, **kwargs)
data_disk = azure_data_disk

class azure_sql_database_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_sql_database_server', _label, **kwargs)
sql_database_server = azure_sql_database_server

class azure_sql_database_server_firewall_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_sql_database_server_firewall_rule', _label, **kwargs)
sql_database_server_firewall_rule = azure_sql_database_server_firewall_rule

class azure_sql_database_service(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_sql_database_service', _label, **kwargs)
sql_database_service = azure_sql_database_service

class azure_hosted_service(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_hosted_service', _label, **kwargs)
hosted_service = azure_hosted_service

class azure_storage_service(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_storage_service', _label, **kwargs)
storage_service = azure_storage_service

class azure_storage_container(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_storage_container', _label, **kwargs)
storage_container = azure_storage_container

class azure_storage_blob(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_storage_blob', _label, **kwargs)
storage_blob = azure_storage_blob

class azure_storage_queue(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_storage_queue', _label, **kwargs)
storage_queue = azure_storage_queue

class azure_virtual_network(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_virtual_network', _label, **kwargs)
virtual_network = azure_virtual_network

class azure_dns_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_dns_server', _label, **kwargs)
dns_server = azure_dns_server

class azure_local_network_connection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_local_network_connection', _label, **kwargs)
local_network_connection = azure_local_network_connection

class azure_security_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_security_group', _label, **kwargs)
security_group = azure_security_group

class azure_security_group_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('azure_security_group_rule', _label, **kwargs)
security_group_rule = azure_security_group_rule

