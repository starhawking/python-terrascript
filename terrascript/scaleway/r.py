from terrascript import Resource
class scaleway_bucket(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_bucket', _label, **kwargs)
bucket = scaleway_bucket

class scaleway_compute_instance_ip(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_compute_instance_ip', _label, **kwargs)
compute_instance_ip = scaleway_compute_instance_ip

class scaleway_compute_instance_volume(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_compute_instance_volume', _label, **kwargs)
compute_instance_volume = scaleway_compute_instance_volume

class scaleway_compute_instance_security_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_compute_instance_security_group', _label, **kwargs)
compute_instance_security_group = scaleway_compute_instance_security_group

class scaleway_compute_instance_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_compute_instance_server', _label, **kwargs)
compute_instance_server = scaleway_compute_instance_server

class scaleway_compute_instance_placement_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_compute_instance_placement_group', _label, **kwargs)
compute_instance_placement_group = scaleway_compute_instance_placement_group

class scaleway_storage_object_bucket(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_storage_object_bucket', _label, **kwargs)
storage_object_bucket = scaleway_storage_object_bucket

class scaleway_user_data(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_user_data', _label, **kwargs)
user_data = scaleway_user_data

class scaleway_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_server', _label, **kwargs)
server = scaleway_server

class scaleway_token(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_token', _label, **kwargs)
token = scaleway_token

class scaleway_ssh_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_ssh_key', _label, **kwargs)
ssh_key = scaleway_ssh_key

class scaleway_ip(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_ip', _label, **kwargs)
ip = scaleway_ip

class scaleway_ip_reverse_dns(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_ip_reverse_dns', _label, **kwargs)
ip_reverse_dns = scaleway_ip_reverse_dns

class scaleway_security_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_security_group', _label, **kwargs)
security_group = scaleway_security_group

class scaleway_security_group_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_security_group_rule', _label, **kwargs)
security_group_rule = scaleway_security_group_rule

class scaleway_volume(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_volume', _label, **kwargs)
volume = scaleway_volume

class scaleway_volume_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('scaleway_volume_attachment', _label, **kwargs)
volume_attachment = scaleway_volume_attachment

