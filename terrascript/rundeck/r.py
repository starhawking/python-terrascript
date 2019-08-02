from terrascript import Resource
class rundeck_project(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rundeck_project', _label, **kwargs)
project = rundeck_project

class rundeck_job(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rundeck_job', _label, **kwargs)
job = rundeck_job

class rundeck_private_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rundeck_private_key', _label, **kwargs)
private_key = rundeck_private_key

class rundeck_public_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rundeck_public_key', _label, **kwargs)
public_key = rundeck_public_key

class rundeck_acl_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rundeck_acl_policy', _label, **kwargs)
acl_policy = rundeck_acl_policy

