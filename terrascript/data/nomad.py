# terrascript/data/nomad.py

import terrascript


class nomad_acl_policy(terrascript.Data):
    pass

class nomad_acl_token(terrascript.Data):
    pass

class nomad_deployments(terrascript.Data):
    pass

class nomad_job(terrascript.Data):
    pass

class nomad_namespaces(terrascript.Data):
    pass

class nomad_regions(terrascript.Data):
    pass


__all__ = [
    'nomad_acl_policy',
    'nomad_acl_token',
    'nomad_deployments',
    'nomad_job',
    'nomad_namespaces',
    'nomad_regions',
]