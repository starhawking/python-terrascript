# terrascript/github/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class github_actions_public_key(terrascript.Data):
    pass


class github_branch(terrascript.Data):
    pass


class github_collaborators(terrascript.Data):
    pass


class github_ip_ranges(terrascript.Data):
    pass


class github_membership(terrascript.Data):
    pass


class github_organization(terrascript.Data):
    pass


class github_organization_team_sync_groups(terrascript.Data):
    pass


class github_release(terrascript.Data):
    pass


class github_repositories(terrascript.Data):
    pass


class github_repository(terrascript.Data):
    pass


class github_repository_milestone(terrascript.Data):
    pass


class github_team(terrascript.Data):
    pass


class github_user(terrascript.Data):
    pass
