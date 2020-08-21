# terrascript/data/nomad.py
import terrascript


class nomad_acl_policy(terrascript.Data):
    pass


class nomad_acl_token(terrascript.Data):
    pass


class nomad_acl_tokens(terrascript.Data):
    pass


class nomad_deployments(terrascript.Data):
    pass


class nomad_job(terrascript.Data):
    pass


class nomad_job_parser(terrascript.Data):
    pass


class nomad_namespace(terrascript.Data):
    pass


class nomad_namespaces(terrascript.Data):
    pass


class nomad_plugin(terrascript.Data):
    pass


class nomad_plugins(terrascript.Data):
    pass


class nomad_regions(terrascript.Data):
    pass


class nomad_volumes(terrascript.Data):
    pass


__all__ = [
    "nomad_acl_policy",
    "nomad_acl_token",
    "nomad_acl_tokens",
    "nomad_deployments",
    "nomad_job",
    "nomad_job_parser",
    "nomad_namespace",
    "nomad_namespaces",
    "nomad_plugin",
    "nomad_plugins",
    "nomad_regions",
    "nomad_volumes",
]
