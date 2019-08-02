"""This test file will import all generated p/r.py code for sanity checking."""
import pkgutil
import terrascript

from importlib import import_module


def test_sanity():
    for importer, modname, ispkg in pkgutil.iter_modules(terrascript.__path__):
        if ispkg:
            import_module(".d", "terrascript." + modname)
            import_module(".r", "terrascript." + modname)
