from terrascript import Resource
class gitlab_branch_protection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_branch_protection', _label, **kwargs)
branch_protection = gitlab_branch_protection

class gitlab_tag_protection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_tag_protection', _label, **kwargs)
tag_protection = gitlab_tag_protection

class gitlab_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_group', _label, **kwargs)
group = gitlab_group

class gitlab_project(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_project', _label, **kwargs)
project = gitlab_project

class gitlab_label(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_label', _label, **kwargs)
label = gitlab_label

class gitlab_pipeline_schedule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_pipeline_schedule', _label, **kwargs)
pipeline_schedule = gitlab_pipeline_schedule

class gitlab_pipeline_trigger(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_pipeline_trigger', _label, **kwargs)
pipeline_trigger = gitlab_pipeline_trigger

class gitlab_project_hook(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_project_hook', _label, **kwargs)
project_hook = gitlab_project_hook

class gitlab_deploy_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_deploy_key', _label, **kwargs)
deploy_key = gitlab_deploy_key

class gitlab_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_user', _label, **kwargs)
user = gitlab_user

class gitlab_project_membership(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_project_membership', _label, **kwargs)
project_membership = gitlab_project_membership

class gitlab_group_membership(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_group_membership', _label, **kwargs)
group_membership = gitlab_group_membership

class gitlab_project_variable(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_project_variable', _label, **kwargs)
project_variable = gitlab_project_variable

class gitlab_group_variable(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_group_variable', _label, **kwargs)
group_variable = gitlab_group_variable

class gitlab_project_cluster(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_project_cluster', _label, **kwargs)
project_cluster = gitlab_project_cluster

class gitlab_service_slack(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_service_slack', _label, **kwargs)
service_slack = gitlab_service_slack

class gitlab_service_jira(Resource):
    def __init__(self, _label, **kwargs): super().__init__('gitlab_service_jira', _label, **kwargs)
service_jira = gitlab_service_jira

