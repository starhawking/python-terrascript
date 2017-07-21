"""
terrascript/__init__.py

Base classes and functions that are used elsewhere in
this project.

"""

INDENT = 2
"""JSON indentation level."""

SORT = True
"""Whether to sort keys when generating JSON."""

from collections import defaultdict


CONFIG = {
    "data": defaultdict(dict),
    "resource": defaultdict(dict),
    "variable": dict(),
    "module": dict()
}

def dump():
    """Return the JSON representaion of CONFIG."""
    import json
    import copy

    # Work on copy of CONFIG but with unused top-level elements removed.
    #
    config = {k: v for k,v in CONFIG.items() if v}
    return json.dumps(config, indent=INDENT, sort_keys=SORT, default=lambda v: str(v))


def validate():
    """Validate a Terraform configuration."""
    import tempfile
    import subprocess

    config = dump()
    tmpdir = tempfile.mkdtemp()
    tmpfile = tempfile.NamedTemporaryFile(mode='w', dir=tmpdir, suffix='.tf.json', delete=False)

    tmpfile.write(config)
    tmpfile.flush()

    proc = subprocess.Popen(['terraform','validate'], cwd=tmpdir)
    proc.communicate()
    return proc.returncode == 0



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

    def __repr__(self):
        """Non-interpolated reference: ``TYPE.NAME``, such as ``aws_instance.web``."""
        return '{}.{}'.format(self._type, self._name)


class _data(_base):
    """Base class for data sources."""
    _class = 'data'

    # TODO: Work-around for https://github.com/mjuenema/python-terrascript/issues/3
    def __init__(self, name, **kwargs):
        if not 'type' in kwargs:
            kwargs['type'] = 'string'
        if not 'description' in kwargs:
            kwargs['description'] = ''
        super(_data, self).__init__(name, **kwargs)


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

    def __repr__(self):
        """Non-interpolated reference: ``module.NAME``, such as ``module.foo``."""
        return 'module.{}'.format(self._name)

    def __getattr__(self, name):
        return '${{module.{}.{}}}'.format(self._name, name)


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
            return "${{var.{}[\"{}\"]}}".format(self._name, i)


__all__ = ['CONFIG', 'dump', 'validate',
           'resource', 'data', 'module', 'variable']
