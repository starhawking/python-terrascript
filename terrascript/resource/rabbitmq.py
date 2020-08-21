# terrascript/resource/rabbitmq.py
import terrascript


class rabbitmq_binding(terrascript.Resource):
    pass


class rabbitmq_exchange(terrascript.Resource):
    pass


class rabbitmq_permissions(terrascript.Resource):
    pass


class rabbitmq_topic_permissions(terrascript.Resource):
    pass


class rabbitmq_federation_upstream(terrascript.Resource):
    pass


class rabbitmq_policy(terrascript.Resource):
    pass


class rabbitmq_queue(terrascript.Resource):
    pass


class rabbitmq_user(terrascript.Resource):
    pass


class rabbitmq_vhost(terrascript.Resource):
    pass


class rabbitmq_shovel(terrascript.Resource):
    pass


__all__ = [
    "rabbitmq_binding",
    "rabbitmq_exchange",
    "rabbitmq_permissions",
    "rabbitmq_topic_permissions",
    "rabbitmq_federation_upstream",
    "rabbitmq_policy",
    "rabbitmq_queue",
    "rabbitmq_user",
    "rabbitmq_vhost",
    "rabbitmq_shovel",
]
