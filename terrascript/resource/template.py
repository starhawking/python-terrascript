# terrascript/resource/template.py
import terrascript


class template_cloudinit_config(terrascript.Resource):
    pass


class template_dir(terrascript.Resource):
    pass


class template_file(terrascript.Resource):
    pass

__all__ = [
    "template_cloudinit_config",
    "template_dir",
    "template_file",
]
