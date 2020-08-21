# terrascript/resource/gitlab.py
import terrascript


class gitlab_branch_protection(terrascript.Resource):
    pass


class gitlab_tag_protection(terrascript.Resource):
    pass


class gitlab_group(terrascript.Resource):
    pass


class gitlab_project(terrascript.Resource):
    pass


class gitlab_label(terrascript.Resource):
    pass


class gitlab_group_label(terrascript.Resource):
    pass


class gitlab_pipeline_schedule(terrascript.Resource):
    pass


class gitlab_pipeline_schedule_variable(terrascript.Resource):
    pass


class gitlab_pipeline_trigger(terrascript.Resource):
    pass


class gitlab_project_hook(terrascript.Resource):
    pass


class gitlab_project_push_rules(terrascript.Resource):
    pass


class gitlab_deploy_key(terrascript.Resource):
    pass


class gitlab_deploy_key_enable(terrascript.Resource):
    pass


class gitlab_deploy_token(terrascript.Resource):
    pass


class gitlab_user(terrascript.Resource):
    pass


class gitlab_project_membership(terrascript.Resource):
    pass


class gitlab_group_membership(terrascript.Resource):
    pass


class gitlab_project_variable(terrascript.Resource):
    pass


class gitlab_group_variable(terrascript.Resource):
    pass


class gitlab_project_cluster(terrascript.Resource):
    pass


class gitlab_service_slack(terrascript.Resource):
    pass


class gitlab_service_jira(terrascript.Resource):
    pass


class gitlab_service_github(terrascript.Resource):
    pass


class gitlab_project_share_group(terrascript.Resource):
    pass


class gitlab_group_cluster(terrascript.Resource):
    pass


class gitlab_group_ldap_link(terrascript.Resource):
    pass


__all__ = [
    "gitlab_branch_protection",
    "gitlab_tag_protection",
    "gitlab_group",
    "gitlab_project",
    "gitlab_label",
    "gitlab_group_label",
    "gitlab_pipeline_schedule",
    "gitlab_pipeline_schedule_variable",
    "gitlab_pipeline_trigger",
    "gitlab_project_hook",
    "gitlab_project_push_rules",
    "gitlab_deploy_key",
    "gitlab_deploy_key_enable",
    "gitlab_deploy_token",
    "gitlab_user",
    "gitlab_project_membership",
    "gitlab_group_membership",
    "gitlab_project_variable",
    "gitlab_group_variable",
    "gitlab_project_cluster",
    "gitlab_service_slack",
    "gitlab_service_jira",
    "gitlab_service_github",
    "gitlab_project_share_group",
    "gitlab_group_cluster",
    "gitlab_group_ldap_link",
]
