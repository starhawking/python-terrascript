"""
terrascript/__init__.py

Base classes and functions that are used elsewhere in
this project.

"""

INDENT = 2
"""JSON indentation level."""

import atexit
from collections import defaultdict, UserString


CONFIG = {
    "data": defaultdict(dict),
    "resource": defaultdict(dict),
    "variable": dict(),
    "module": dict()
}


class _base(object):
    _class = None
    """One of 'resource', 'data' or 'module'."""

    _type = None
    """The resource type, e.g. 'aws_instance'."""

    _name = None
    """The name of this resource, e.g. 'my_ec2_instance'."""

    def __init__(self, name, **kwargs):
        if not self._type:
            self._type = self.__class__.__name__
        self._name = name

        CONFIG[self._class][self._type][self._name] = kwargs

    def __getattr__(self, name):
        if self._class == 'resource':
            return '${{{}.{}.{}}}'.format(self._type, self._name, name)
        else:
            return '${{{}.{}.{}.{}}}'.format(self._class, self._type, self._name, name)


class _resource(_base):
    """Base class for resources."""
    _class = 'resource'


class _data(_base):
    """Base class for data sources."""
    _class = 'data'


class resource(_base):
    """Class for creating a resource for which no convenience wrapper exists."""
    _class = 'resource'
    def __init__(self, type_, name, **kwargs):
        self._type = type_
        super(resource, self).__init__(name, **kwargs)


class data(_base):
    """Class for creating a data source for which no convenience wrapper exists."""
    _class = 'data'
    def __init__(self, type_, name, **kwargs):
        self._type = type_
        super(data, self).__init__(name, **kwargs)


class module(_base):
    """Class for modules."""

    def __init__(self, name, **kwargs):
        self._name = name
        CONFIG['module'][self._name] = kwargs


class variable(object):
    """Class for variables."""

    def __init__(self, name, **kwargs):
        self._name = name
        CONFIG['variable'][self._name] = kwargs

    def __repr__(self):
        return '${{var.{}}}'.format(self._name)

    def __getitem__(self, i):
        if isinstance(i, int):
            # "${var.NAME[i]}"
            return '${{var.{}[{}]}}'.format(self._name, i)
        else:
            # "${var.NAME["i"]}"
            return '${{var.{}["{}"]}}'.format(self._name, i)

def _serialise(v):
    return str(v)

def dump():
    import json
    return json.dumps(CONFIG, indent=INDENT, default=_serialise)


__all__ = ['CONFIG', 'resource', 'data', 'module', 'variable']
