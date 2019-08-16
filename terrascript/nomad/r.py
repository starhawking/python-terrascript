from terrascript import Resource
class nomad_acl_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('nomad_acl_policy', _label, **kwargs)
acl_policy = nomad_acl_policy

class nomad_acl_token(Resource):
    def __init__(self, _label, **kwargs): super().__init__('nomad_acl_token', _label, **kwargs)
acl_token = nomad_acl_token

class nomad_job(Resource):
    def __init__(self, _label, **kwargs): super().__init__('nomad_job', _label, **kwargs)
job = nomad_job

class nomad_namespace(Resource):
    def __init__(self, _label, **kwargs): super().__init__('nomad_namespace', _label, **kwargs)
namespace = nomad_namespace

class nomad_quota_specification(Resource):
    def __init__(self, _label, **kwargs): super().__init__('nomad_quota_specification', _label, **kwargs)
quota_specification = nomad_quota_specification

class nomad_sentinel_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('nomad_sentinel_policy', _label, **kwargs)
sentinel_policy = nomad_sentinel_policy

