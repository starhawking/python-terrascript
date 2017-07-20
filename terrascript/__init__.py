"""
terrascript/__init__.py

Base classes and functions that are used elsewhere in
this project.

"""

INDENT = 2
"""JSON indentation level."""

import json
from collections import defaultdict, OrderedDict

CONFIG = {
    "data": defaultdict(dict),
    "resource": defaultdict(dict)
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
    """Base class for modules."""
    _class = 'module'


__all__ = ['CONFIG', 'resource', 'data', 'module']
