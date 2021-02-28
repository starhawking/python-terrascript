# terrascript/rabbitmq/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class rabbitmq_binding(terrascript.Resource):
    pass


class rabbitmq_exchange(terrascript.Resource):
    pass


class rabbitmq_federation_upstream(terrascript.Resource):
    pass


class rabbitmq_permissions(terrascript.Resource):
    pass


class rabbitmq_policy(terrascript.Resource):
    pass


class rabbitmq_queue(terrascript.Resource):
    pass


class rabbitmq_shovel(terrascript.Resource):
    pass


class rabbitmq_topic_permissions(terrascript.Resource):
    pass


class rabbitmq_user(terrascript.Resource):
    pass


class rabbitmq_vhost(terrascript.Resource):
    pass
