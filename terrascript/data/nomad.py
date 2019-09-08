# terrascript/data/nomad.py

import terrascript


class nomad_job(terrascript.Data):
    pass

class nomad_deployments(terrascript.Data):
    pass

class nomad_namespaces(terrascript.Data):
    pass

class nomad_regions(terrascript.Data):
    pass


__all__ = [
    'nomad_job',
    'nomad_deployments',
    'nomad_namespaces',
    'nomad_regions',
]