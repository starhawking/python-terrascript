"""
terrascript/__init__.py

Base classes and functions that are used elsewhere in
this project.

"""

import collections

def _fmtk(k):
    return '{}'.format(k)

def _fmtv(v):
    if isinstance(v, bool):
        return str(v).lower()
    elif isinstance(v, list):
        return str(v).replace("'", '"')
    elif isinstance(v, str):
        return '"{}"'.format(v)
    else:
        return '{}'.format(v)


def _print_list(n, l):
    print('  {} = {}'.format(_fmtk(n), _fmtv(l)))

def _print_bool(n, b):
    print('  {} = {}'.format(_fmtk(n), _fmtv(b)))

def _print_string(n, s):
    print('  {} = {}'.format(_fmtk(n), _fmtv(s)))

def _print_dict(n, d):
    print('  {} = {{'.format(n))
    d = collections.OrderedDict(sorted(d.items()))
    for k,v in d.items():
        print('    {} = {}'.format(_fmtk(k), _fmtv(v)))
    print('  }')


class _base(object):
    """

    """

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

        print('{} "{}" "{}" {{'.format(self._class, self._type, self._name))
        for k,v in kwargs.items():
            if isinstance(v, list):
                _print_list(k, v)
            elif isinstance(v, bool):
                _print_bool(k, v)
            elif isinstance(v, dict):
                _print_dict(k, v)
            else:
                _print_string(k, v)
        print('}\n')

    def _ref(self, ref):
        if self._class == 'resource':
            return '${{{}.{}.{}}}'.format(self._type, self._name, ref)
        else:
            return '${{{}.{}.{}.{}}}'.format(self._class, self._type, self._name, ref)

    def __getattr__(self, attr):
        return self._ref(attr)

    def __str__(self):
        return self._ref('id')


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


if __name__ == '__main__':
    ami1 = aws_ami('ubuntu', most_recent=True, owners = ["099720109477"],
                  filter={'name': "NAME", 'values': ['VALUE1', 'VALUE2']})

    i1 = aws_instance('aws_instance_1', ami=ami1)
    i2 = aws_instance('aws_instance_2', otherid=i1, otherami=i1.ami)

    ami2 = data('aws_ami', 'centos', most_recent=True, owners = ["099720109477"])
    i3 = resource('aws_instance', 'aws_instance_1', ami=ami2)


