# terrascript/resource/chef.py
import terrascript


class chef_acl(terrascript.Resource):
    pass


class chef_client(terrascript.Resource):
    pass


class chef_cookbook(terrascript.Resource):
    pass


class chef_data_bag(terrascript.Resource):
    pass


class chef_data_bag_item(terrascript.Resource):
    pass


class chef_environment(terrascript.Resource):
    pass


class chef_node(terrascript.Resource):
    pass


class chef_role(terrascript.Resource):
    pass


__all__ = [
    "chef_acl",
    "chef_client",
    "chef_cookbook",
    "chef_data_bag",
    "chef_data_bag_item",
    "chef_environment",
    "chef_node",
    "chef_role",
]
