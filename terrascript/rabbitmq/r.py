from terrascript import Resource
class rabbitmq_binding(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rabbitmq_binding', _label, **kwargs)
binding = rabbitmq_binding

class rabbitmq_exchange(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rabbitmq_exchange', _label, **kwargs)
exchange = rabbitmq_exchange

class rabbitmq_permissions(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rabbitmq_permissions', _label, **kwargs)
permissions = rabbitmq_permissions

class rabbitmq_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rabbitmq_policy', _label, **kwargs)
policy = rabbitmq_policy

class rabbitmq_queue(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rabbitmq_queue', _label, **kwargs)
queue = rabbitmq_queue

class rabbitmq_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rabbitmq_user', _label, **kwargs)
user = rabbitmq_user

class rabbitmq_vhost(Resource):
    def __init__(self, _label, **kwargs): super().__init__('rabbitmq_vhost', _label, **kwargs)
vhost = rabbitmq_vhost

