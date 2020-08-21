# terrascript/resource/nomad.py
import terrascript


class nomad_acl_policy(terrascript.Resource):
    pass


class nomad_acl_token(terrascript.Resource):
    pass


class nomad_job(terrascript.Resource):
    pass


class nomad_namespace(terrascript.Resource):
    pass


class nomad_quota_specification(terrascript.Resource):
    pass


class nomad_sentinel_policy(terrascript.Resource):
    pass


class nomad_volume(terrascript.Resource):
    pass


__all__ = [
    "nomad_acl_policy",
    "nomad_acl_token",
    "nomad_job",
    "nomad_namespace",
    "nomad_quota_specification",
    "nomad_sentinel_policy",
    "nomad_volume",
]
