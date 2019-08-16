from terrascript import Resource
class bitbucket_hook(Resource):
    def __init__(self, _label, **kwargs): super().__init__('bitbucket_hook', _label, **kwargs)
hook = bitbucket_hook

class bitbucket_default_reviewers(Resource):
    def __init__(self, _label, **kwargs): super().__init__('bitbucket_default_reviewers', _label, **kwargs)
default_reviewers = bitbucket_default_reviewers

class bitbucket_repository(Resource):
    def __init__(self, _label, **kwargs): super().__init__('bitbucket_repository', _label, **kwargs)
repository = bitbucket_repository

