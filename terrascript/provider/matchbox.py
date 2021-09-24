# terrascript/provider/matchbox.py
import terrascript


class matchbox(terrascript.Provider):
    """Terraform provider for on-premise / bare-metal via Matchbox"""

    __description__ = "Terraform provider for on-premise / bare-metal via Matchbox"
    __version__ = "0.4.1"


__all__ = ["matchbox"]
