from terrascript import Resource
class chef_acl(Resource):
    def __init__(self, _label, **kwargs): super().__init__('chef_acl', _label, **kwargs)
acl = chef_acl

class chef_client(Resource):
    def __init__(self, _label, **kwargs): super().__init__('chef_client', _label, **kwargs)
client = chef_client

class chef_cookbook(Resource):
    def __init__(self, _label, **kwargs): super().__init__('chef_cookbook', _label, **kwargs)
cookbook = chef_cookbook

class chef_data_bag(Resource):
    def __init__(self, _label, **kwargs): super().__init__('chef_data_bag', _label, **kwargs)
data_bag = chef_data_bag

class chef_data_bag_item(Resource):
    def __init__(self, _label, **kwargs): super().__init__('chef_data_bag_item', _label, **kwargs)
data_bag_item = chef_data_bag_item

class chef_environment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('chef_environment', _label, **kwargs)
environment = chef_environment

class chef_node(Resource):
    def __init__(self, _label, **kwargs): super().__init__('chef_node', _label, **kwargs)
node = chef_node

class chef_role(Resource):
    def __init__(self, _label, **kwargs): super().__init__('chef_role', _label, **kwargs)
role = chef_role

