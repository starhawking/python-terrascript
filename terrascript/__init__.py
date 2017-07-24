"""
terrascript/__init__.py

Base classes and functions that are used elsewhere in
this project.

"""

INDENT = 2
"""JSON indentation level."""

SORT = True
"""Whether to sort keys when generating JSON."""

from collections import defaultdict, UserDict



class CONFIG(dict):
    def __getitem__(self, key):
        try:
            return super(CONFIG, self).__getitem__(key)
        except KeyError:
            if key in ['data', 'resource']:
                super(CONFIG, self).__setitem__(key, defaultdict(dict))
            elif key in ['variable', 'module']:
                super(CONFIG, self).__setitem__(key, dict)
            else:
                raise KeyError(key)
                
        return super(CONFIG, self).__getitem__(key)
            

config = CONFIG()

def dump():
    """Return the JSON representaion of config."""
    import json

    # Work on copy of CONFIG but with unused top-level elements removed.
    #
    config_copy = {k: v for k,v in config.items() if v}
    return json.dumps(config_copy, indent=INDENT, sort_keys=SORT, default=lambda v: str(v))


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
    """One of 'resource', 'data', 'module', etc."""

    _type = None
    """The resource type, e.g. 'aws_instance'."""

    _name = None
    """The name of this resource, e.g. 'my_ec2_instance'."""

    def __init__(self, name, **kwargs):
        if not self._type:
            self._type = self.__class__.__name__
        self._name = name

        if self._class in ['resource', 'data']:
            config[self._class][self._type][self._name] = kwargs
        else:
            config[self._class][self._name] = kwargs

    def __getattr__(self, name):
        """References to attributes."""
        if self._class == 'resource':
            return '${{{}.{}.{}}}'.format(self._type, self._name, name)
        elif self._class == 'module':
            return '${{module.{}.{}}}'.format(self._name, name)
        else:
            return '${{{}.{}.{}.{}}}'.format(self._class, self._type, self._name, name)
            
    def __getitem__(self, i):
        if isinstance(i, int):
            # "${var.NAME[i]}"
            return '${{var.{}[{}]}}'.format(self._name, i)
        else:
            # "${var.NAME["i"]}"
            return "${{var.{}[\"{}\"]}}".format(self._name, i)

    def __repr__(self):
        """References to objects."""
        if self._class == 'resource':
            """Non-interpolated reference to a resource, e.g. ``aws_instance.web``."""
            return '{}.{}'.format(self._type, self._name)
        elif self._class == 'variable':
            """Interpolated reference to a variable, e.g. ``var.http_port``."""
            return '${{var.{}}}'.format(self._name)
        else:
            """Non-interpolated reference to a non-resource, e.g. ``module.http``."""
            return '{}.{}'.format(self._class, self._name)


class _resource(_base):
    """Base class for resources."""
    _class = 'resource'



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
    
    _class = 'module'


class variable(_base):
    """Class for variables."""
    
    _class = 'variable'



__all__ = ['config', 'dump', 'validate',
           'resource', 'data', 'module', 'variable']
