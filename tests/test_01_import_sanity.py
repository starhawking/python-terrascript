"""This test file will import all generated p/r.py code for sanity checking."""
import pkgutil
import unittest

import terrascript

from importlib import import_module

import sys


@unittest.skipIf(sys.version_info < (3, 5), "import_module doesn't work properly in Python 3.4")
def test_sanity():
    for importer, modname, ispkg in pkgutil.iter_modules(terrascript.__path__):
        if ispkg:
            import_module(".d", "terrascript." + modname)
            import_module(".r", "terrascript." + modname)
