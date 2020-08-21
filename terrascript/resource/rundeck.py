# terrascript/resource/rundeck.py
import terrascript


class rundeck_project(terrascript.Resource):
    pass


class rundeck_job(terrascript.Resource):
    pass


class rundeck_private_key(terrascript.Resource):
    pass


class rundeck_public_key(terrascript.Resource):
    pass


class rundeck_acl_policy(terrascript.Resource):
    pass


__all__ = [
    "rundeck_project",
    "rundeck_job",
    "rundeck_private_key",
    "rundeck_public_key",
    "rundeck_acl_policy",
]
