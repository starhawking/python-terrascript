from terrascript import Data
class consul_agent_self(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_agent_self', _label, **kwargs)
agent_self = consul_agent_self

class consul_agent_config(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_agent_config', _label, **kwargs)
agent_config = consul_agent_config

class consul_autopilot_health(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_autopilot_health', _label, **kwargs)
autopilot_health = consul_autopilot_health

class consul_nodes(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_nodes', _label, **kwargs)
nodes = consul_nodes

class consul_service(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_service', _label, **kwargs)
service = consul_service

class consul_service_health(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_service_health', _label, **kwargs)
service_health = consul_service_health

class consul_services(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_services', _label, **kwargs)
services = consul_services

class consul_keys(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_keys', _label, **kwargs)
keys = consul_keys

class consul_key_prefix(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_key_prefix', _label, **kwargs)
key_prefix = consul_key_prefix

class consul_acl_token(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_acl_token', _label, **kwargs)
acl_token = consul_acl_token

class consul_acl_token_secret_id(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_acl_token_secret_id', _label, **kwargs)
acl_token_secret_id = consul_acl_token_secret_id

class consul_catalog_nodes(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_catalog_nodes', _label, **kwargs)
catalog_nodes = consul_catalog_nodes

class consul_catalog_service(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_catalog_service', _label, **kwargs)
catalog_service = consul_catalog_service

class consul_catalog_services(Data):
    def __init__(self, _label, **kwargs): super().__init__('consul_catalog_services', _label, **kwargs)
catalog_services = consul_catalog_services

