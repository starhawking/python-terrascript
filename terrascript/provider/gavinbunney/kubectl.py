# terrascript/provider/gavinbunney/kubectl.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:20:27 UTC)

import terrascript


class kubectl(terrascript.Provider):
    """Terraform provider to handle raw kubernetes manifest yaml files"""

    __description__ = "Terraform provider to handle raw kubernetes manifest yaml files"
    __namespace__ = "gavinbunney"
    __name__ = "kubectl"
    __source__ = "https://github.com/gavinbunney/terraform-provider-kubectl"
    __version__ = "1.11.3"
    __published__ = "2021-08-02T22:15:28Z"
    __tier__ = "community"


__all__ = ["kubectl"]
