from terrascript import Data
class nomad_job(Data):
    def __init__(self, _label, **kwargs): super().__init__('nomad_job', _label, **kwargs)
job = nomad_job

class nomad_deployments(Data):
    def __init__(self, _label, **kwargs): super().__init__('nomad_deployments', _label, **kwargs)
deployments = nomad_deployments

class nomad_namespaces(Data):
    def __init__(self, _label, **kwargs): super().__init__('nomad_namespaces', _label, **kwargs)
namespaces = nomad_namespaces

class nomad_regions(Data):
    def __init__(self, _label, **kwargs): super().__init__('nomad_regions', _label, **kwargs)
regions = nomad_regions

