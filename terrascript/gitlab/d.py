from terrascript import Data
class gitlab_group(Data):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_group', _label, **kwargs)
group = gitlab_group

class gitlab_project(Data):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_project', _label, **kwargs)
project = gitlab_project

class gitlab_user(Data):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_user', _label, **kwargs)
user = gitlab_user

class gitlab_users(Data):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_users', _label, **kwargs)
users = gitlab_users

