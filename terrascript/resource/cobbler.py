# terrascript/resource/cobbler.py
import terrascript


class cobbler_distro(terrascript.Resource):
    pass


class cobbler_kickstart_file(terrascript.Resource):
    pass


class cobbler_profile(terrascript.Resource):
    pass


class cobbler_repo(terrascript.Resource):
    pass


class cobbler_snippet(terrascript.Resource):
    pass


class cobbler_system(terrascript.Resource):
    pass


__all__ = [
    "cobbler_distro",
    "cobbler_kickstart_file",
    "cobbler_profile",
    "cobbler_repo",
    "cobbler_snippet",
    "cobbler_system",
]
