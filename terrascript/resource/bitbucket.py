# terrascript/resource/bitbucket.py
import terrascript


class bitbucket_hook(terrascript.Resource):
    pass


class bitbucket_default_reviewers(terrascript.Resource):
    pass


class bitbucket_repository(terrascript.Resource):
    pass


class bitbucket_repository_variable(terrascript.Resource):
    pass


class bitbucket_project(terrascript.Resource):
    pass


class bitbucket_branch_restriction(terrascript.Resource):
    pass


__all__ = [
    "bitbucket_hook",
    "bitbucket_default_reviewers",
    "bitbucket_repository",
    "bitbucket_repository_variable",
    "bitbucket_project",
    "bitbucket_branch_restriction",
]
