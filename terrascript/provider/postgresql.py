# terrascript/provider/postgresql.py
import terrascript


class postgresql(terrascript.Provider):
    """Terraform PostgreSQL provider"""

    __description__ = "Terraform PostgreSQL provider"
    __version__ = "1.11.2"


__all__ = ["postgresql"]
