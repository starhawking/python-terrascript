# terrascript/resource/azure.py
import terrascript


class azure_instance(terrascript.Resource):
    pass


class azure_affinity_group(terrascript.Resource):
    pass


class azure_data_disk(terrascript.Resource):
    pass


class azure_sql_database_server(terrascript.Resource):
    pass


class azure_sql_database_server_firewall_rule(terrascript.Resource):
    pass


class azure_sql_database_service(terrascript.Resource):
    pass


class azure_hosted_service(terrascript.Resource):
    pass


class azure_storage_service(terrascript.Resource):
    pass


class azure_storage_container(terrascript.Resource):
    pass


class azure_storage_blob(terrascript.Resource):
    pass


class azure_storage_queue(terrascript.Resource):
    pass


class azure_virtual_network(terrascript.Resource):
    pass


class azure_dns_server(terrascript.Resource):
    pass


class azure_local_network_connection(terrascript.Resource):
    pass


class azure_security_group(terrascript.Resource):
    pass


class azure_security_group_rule(terrascript.Resource):
    pass


__all__ = [
    "azure_instance",
    "azure_affinity_group",
    "azure_data_disk",
    "azure_sql_database_server",
    "azure_sql_database_server_firewall_rule",
    "azure_sql_database_service",
    "azure_hosted_service",
    "azure_storage_service",
    "azure_storage_container",
    "azure_storage_blob",
    "azure_storage_queue",
    "azure_virtual_network",
    "azure_dns_server",
    "azure_local_network_connection",
    "azure_security_group",
    "azure_security_group_rule",
]
