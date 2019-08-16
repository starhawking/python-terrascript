from terrascript import Resource
class github_branch_protection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_branch_protection', _label, **kwargs)
branch_protection = github_branch_protection

class github_issue_label(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_issue_label', _label, **kwargs)
issue_label = github_issue_label

class github_membership(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_membership', _label, **kwargs)
membership = github_membership

class github_organization_block(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_organization_block', _label, **kwargs)
organization_block = github_organization_block

class github_organization_project(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_organization_project', _label, **kwargs)
organization_project = github_organization_project

class github_organization_webhook(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_organization_webhook', _label, **kwargs)
organization_webhook = github_organization_webhook

class github_project_column(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_project_column', _label, **kwargs)
project_column = github_project_column

class github_repository_collaborator(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_repository_collaborator', _label, **kwargs)
repository_collaborator = github_repository_collaborator

class github_repository_deploy_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_repository_deploy_key', _label, **kwargs)
repository_deploy_key = github_repository_deploy_key

class github_repository_project(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_repository_project', _label, **kwargs)
repository_project = github_repository_project

class github_repository_webhook(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_repository_webhook', _label, **kwargs)
repository_webhook = github_repository_webhook

class github_repository(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_repository', _label, **kwargs)
repository = github_repository

class github_team_membership(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_team_membership', _label, **kwargs)
team_membership = github_team_membership

class github_team_repository(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_team_repository', _label, **kwargs)
team_repository = github_team_repository

class github_team(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_team', _label, **kwargs)
team = github_team

class github_user_gpg_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_user_gpg_key', _label, **kwargs)
user_gpg_key = github_user_gpg_key

class github_user_invitation_accepter(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_user_invitation_accepter', _label, **kwargs)
user_invitation_accepter = github_user_invitation_accepter

class github_user_ssh_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('github_user_ssh_key', _label, **kwargs)
user_ssh_key = github_user_ssh_key

