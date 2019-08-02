"""This test file will import all generated p/r.py code for sanity checking."""
import pkgutil
import terrascript

from importlib import import_module


def test_sanity():
    for module_info in pkgutil.iter_modules(terrascript.__path__):
        if module_info.ispkg:
            import_module(".d", "terrascript." + module_info.name)
            import_module(".r", "terrascript." + module_info.name)
