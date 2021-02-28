# terrascript/github/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class github_actions_organization_secret(terrascript.Resource):
    pass


class github_actions_secret(terrascript.Resource):
    pass


class github_branch(terrascript.Resource):
    pass


class github_branch_default(terrascript.Resource):
    pass


class github_branch_protection(terrascript.Resource):
    pass


class github_branch_protection_v3(terrascript.Resource):
    pass


class github_issue_label(terrascript.Resource):
    pass


class github_membership(terrascript.Resource):
    pass


class github_organization_block(terrascript.Resource):
    pass


class github_organization_project(terrascript.Resource):
    pass


class github_organization_webhook(terrascript.Resource):
    pass


class github_project_card(terrascript.Resource):
    pass


class github_project_column(terrascript.Resource):
    pass


class github_repository(terrascript.Resource):
    pass


class github_repository_collaborator(terrascript.Resource):
    pass


class github_repository_deploy_key(terrascript.Resource):
    pass


class github_repository_file(terrascript.Resource):
    pass


class github_repository_milestone(terrascript.Resource):
    pass


class github_repository_project(terrascript.Resource):
    pass


class github_repository_webhook(terrascript.Resource):
    pass


class github_team(terrascript.Resource):
    pass


class github_team_membership(terrascript.Resource):
    pass


class github_team_repository(terrascript.Resource):
    pass


class github_team_sync_group_mapping(terrascript.Resource):
    pass


class github_user_gpg_key(terrascript.Resource):
    pass


class github_user_invitation_accepter(terrascript.Resource):
    pass


class github_user_ssh_key(terrascript.Resource):
    pass
