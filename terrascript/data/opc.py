# terrascript/data/opc.py
import terrascript


class opc_compute_image_list_entry(terrascript.Data):
    pass


class opc_compute_ip_address_reservation(terrascript.Data):
    pass


class opc_compute_ip_reservation(terrascript.Data):
    pass


class opc_compute_machine_image(terrascript.Data):
    pass


class opc_compute_network_interface(terrascript.Data):
    pass


class opc_compute_ssh_key(terrascript.Data):
    pass


class opc_compute_storage_volume_snapshot(terrascript.Data):
    pass


class opc_compute_vnic(terrascript.Data):
    pass


__all__ = [
    "opc_compute_image_list_entry",
    "opc_compute_ip_address_reservation",
    "opc_compute_ip_reservation",
    "opc_compute_machine_image",
    "opc_compute_network_interface",
    "opc_compute_ssh_key",
    "opc_compute_storage_volume_snapshot",
    "opc_compute_vnic",
]
