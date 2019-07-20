"""
terrascript/__init__.py

Base classes and functions that are used elsewhere in
this project.

"""

import logging
import os
import json
from collections import defaultdict, UserDict
import collections.abc

__author__ = 'Markus Juenemann <markus@juenemann.net>'
__version__ = '0.7.0'
__license__ = 'BSD 2-clause "Simplified" License'

INDENT = 2
"""JSON indentation level."""

SORT = True
"""Whether to sort keys when generating JSON."""

DEBUG = False
"""Set to enable some debugging."""

logger = logging.getLogger(__name__)


# THREE_TIER_ITEMS = ['data', 'resource', 'provider']
# TWO_TIER_ITEMS = ['variable', 'module', 'output', 'provisioner']
# ONE_TIER_ITEMS = ['terraform']


class NestedDefaultDict(collections.defaultdict):
    """Version of `collections.defaultdict` that supports
       nested keys, e.g.

         >>>nd = NestedDefaultDict()
         >>>nd[1][2][3] = 123
         >>>nd[1][2][3]
         123

    """

    def __init__(self, *args, **kwargs):
        super(NestedDefaultDict, self).__init__(NestedDefaultDict, *args, **kwargs)


class Block(collections.abc.MutableMapping):
    """A `Block` is a container for other content.
    
       See https://www.terraform.io/docs/configuration/syntax.html#blocks.
       
    """
    def __init__(self, *labels, **args):
        self._labels = labels
        self._args = args

    def __getitem__(self, key):
        return self._args[key]
    
    def __setitem__(self, key, value):
        self._args[key] = value
        
    def __delitem__(self, key):
        del(self._args[key])

    def __len__(self):
        raise NotImplementedError('Instances of %s do not have a length' %
                                  (self.__class__.__name__))

    def __iter__(self):
        for key in self._args:
            yield key
            
    def __str__(self):
        """The `__str__` method is (ab)used to convert to Terraform JSON."""
        
        def _encode(o):
            try:
                return o._args
            except AttributeError:
                raise TypeError(repr(o) + " is not JSON serializable")
                
        return json.dumps(self, default=_encode, indent=INDENT, sort_keys=SORT)
                
    def keys(self):
        return self._args.keys()
    
    def values(self):
        return self._args.values()
    
    def items(self):
        return self._args.items()


class Terrascript(Block):
    """Top-level container for Terraform configurations.
    
       It has neither labels nor arguments.
    """

    def __init__(self):
        super(Terrascript, self).__init__()
        
    def __len__(self):
        # TODO: Possibly return number of items per type, e.g.
        #       {'resource': 3, 'output': 2, ...}
        raise NotImplementedError()
        
    def __add__(self, block):
        
        if isinstance(block, Resource):
            # {
            #  "resource": {
            #    "aws_instance": {                 <== block.__class__.__name__
            #      "example": {                    <== block._labels[0]
            #        "instance_type": "t2.micro",
            #        "ami": "ami-abc123"
            #      }
            #    }
            #   }
            # }

            if not 'resource' in self:
                self['resource'] = NestedDict()
            self['resource'][block.__class__.__name__][block._labels[0]] = block._args

        else:
            raise ValueError('An instance of %s cannot be added to instances of %s' % block.__class__.__name__, self.__class__.__name__)
            
        add = __add__

    def dump(self):
        """The `dump()` method is kept for backwards compatibilty
           as the `__str__()` method returns the JSON representation.

        """

        return str(self)

    def validate(self, delete=True):
        """Validate a Terraform configuration."""
        import tempfile
        import subprocess

        config = self.dump()
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpfile = tempfile.NamedTemporaryFile(mode='w',
                                                  dir=tmpdir,
                                                  suffix='.tf.json',
                                                  delete=delete)

            tmpfile.write(self.dump())
            tmpfile.flush()

            # Download plugins
            proc = subprocess.Popen(['terraform', 'init'], cwd=tmpdir,
                                    stdout=subprocess.PIPE, stderr=None)
            proc.communicate()
            assert proc.returncode == 0

            # Validate configuration
            proc = subprocess.Popen(['terraform',
                                     'validate',
                                     '-check-variables=false'],
                                    cwd=tmpdir,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            stdout, stderr = proc.communicate()

            tmpfile.close()

        return proc.returncode == 0
    
    
class Resource(Block):
    """Base class for actual resource classes.
    
       Derived classes must be named *exactly* like the
       Terraform resource they represent.
          
    """
    
    def __init__(self, label, **args):
        super(Resource, self).__init__(label, **args)


# class _data(_base):
#     """Base class for data sources."""
#     _class = 'data'

#     def __init__(self, obj_name, **kwargs):
#         super(_data, self).__init__(obj_name, **kwargs)


# class resource(_base):
#     """Class for creating a resource for which no convenience wrapper exists."""
#     _class = 'resource'

#     def __init__(self, type_, name, **kwargs):
#         self._type = type_
#         super(resource, self).__init__(name, **kwargs)


# class data(_base):
#     """Class for creating a data source for which no convenience wrapper exists."""
#     _class = 'data'

#     def __init__(self, type_, name, **kwargs):
#         self._type = type_
#         super(data, self).__init__(name, **kwargs)


# class module(_base):
#     _class = 'module'


# class variable(_base):
#     _class = 'variable'


# class output(_base):
#     _class = 'output'


# class provider(_base):
#     _class = 'provider'

#     def __init__(self, name, **kwargs):
#        alias = kwargs.get('alias', '__DEFAULT__')
#        self._type = name
#        super(provider, self).__init__(alias, **kwargs)


# class terraform(_base):
#     _class = 'terraform'
#     def __init__(self, **kwargs):
#         # Terraform does not have a name
#         super(terraform, self).__init__(None, **kwargs)


# class provisioner(UserDict):
#     def __init__(self, type_, **kwargs):
#        self._type = type_
#        self.data = kwargs


# class connection(UserDict):
#     def __init__(self,  **kwargs):
#         self.data = kwargs


# class backend(UserDict):
#     def __init__(self,  name, **kwargs):
#         self.data = {name: kwargs}


# class _function(object):
#     """Terraform function.

#        >>> function.lookup(map, key)
#        "${lookup(map, key)}"

#     """

#     class _function(object):
#         def __init__(self, name):
#             self.name = name

#         def format(self, arg):
#             """Format a function argument."""
#             if isinstance(arg, _base):
#                 return arg.fullname
#             elif isinstance(arg, str):
#                 return '"{}"'.format(arg)
#             else:
#                 return arg

#         def __call__(self, *args):
#             return '${{{}({})}}'.format(self.name, ','.join([self.format(arg) for arg in args]))

#     def __getattr__(self, name):
#         return self._function(name)

# f = fn = func = function = _function()
# """Shortcuts for `function()`."""

__all__ = ['Block', 'Terrascript', 'Resource']
#           'resource', 'data', 'module', 'variable',
#           'output', 'terraform', 'provider', 
#           'provisioner', 'connection', 'backend',
#           'f', 'fn', 'func', 'function']
