from terrascript import Data
class github_collaborators(Data):
    def __init__(self, _label, **kwargs): super().__init__('github_collaborators', _label, **kwargs)
collaborators = github_collaborators

class github_ip_ranges(Data):
    def __init__(self, _label, **kwargs): super().__init__('github_ip_ranges', _label, **kwargs)
ip_ranges = github_ip_ranges

class github_repositories(Data):
    def __init__(self, _label, **kwargs): super().__init__('github_repositories', _label, **kwargs)
repositories = github_repositories

class github_repository(Data):
    def __init__(self, _label, **kwargs): super().__init__('github_repository', _label, **kwargs)
repository = github_repository

class github_team(Data):
    def __init__(self, _label, **kwargs): super().__init__('github_team', _label, **kwargs)
team = github_team

class github_user(Data):
    def __init__(self, _label, **kwargs): super().__init__('github_user', _label, **kwargs)
user = github_user

