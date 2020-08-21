# terrascript/data/ignition.py
import terrascript


class ignition_config(terrascript.Data):
    pass


class ignition_disk(terrascript.Data):
    pass


class ignition_raid(terrascript.Data):
    pass


class ignition_filesystem(terrascript.Data):
    pass


class ignition_file(terrascript.Data):
    pass


class ignition_directory(terrascript.Data):
    pass


class ignition_link(terrascript.Data):
    pass


class ignition_systemd_unit(terrascript.Data):
    pass


class ignition_networkd_unit(terrascript.Data):
    pass


class ignition_user(terrascript.Data):
    pass


class ignition_group(terrascript.Data):
    pass


__all__ = [
    "ignition_config",
    "ignition_disk",
    "ignition_raid",
    "ignition_filesystem",
    "ignition_file",
    "ignition_directory",
    "ignition_link",
    "ignition_systemd_unit",
    "ignition_networkd_unit",
    "ignition_user",
    "ignition_group",
]
