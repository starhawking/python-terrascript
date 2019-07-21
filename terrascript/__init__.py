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
import warnings

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


def _validate(config):
    """Validate a Terraform configuration. 
    
       This used to be a method of the `Terraform` class which is now
       deprecated. Users are encouraged to use the ``config validate``
       command instead.
        
    """
    
    import tempfile
    import subprocess

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpfile = tempfile.NamedTemporaryFile(mode='w',
                                              dir=tmpdir,
                                              suffix='.tf.json')

        tmpfile.write(str(config))
        tmpfile.flush()

        # Download plugins
        proc = subprocess.Popen(['terraform', 'init'], cwd=tmpdir,
                                stdout=subprocess.PIPE, stderr=None)
        proc.communicate()
        assert proc.returncode == 0

        # Validate configuration
        proc = subprocess.Popen(['terraform',
                                 'validate'],
                                cwd=tmpdir,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        proc.communicate()
        
        #raise Exception
        
        tmpfile.close()

    return proc.returncode == 0


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
        
    def __str__(self):
        return json.dumps(dict(self))


class Block(NestedDefaultDict):
    """A `Block` is a container for other content.
    
       See https://www.terraform.io/docs/configuration/syntax.html#blocks.
       
       TODO: Can we make this a NestedDefaultDict?
       
    """
    
    def __init__(self, *labels, **args):
         super(Block, self).__init__()
         self._labels = labels
         self.update(args)
         

class Terrascript(Block):
    """Top-level container for Terraform configurations.
    
       It has neither labels nor arguments.
    """

    def __init__(self):
        super(Terrascript, self).__init__()
        
    def __add__(self, block):        
        
        if type(block) == Resource:
            # Resource can be instantiated directly to add Terraform resources
            # for which no subclass exists in Terrascript.\
            #
               # {
            #  "resource": {
            #    "foobar":       {                 <== block._labels[0]
            #      "example": {                    <== block._labels[1]
            #        "instance_type": "t2.micro",
            #        "ami": "ami-abc123"
            #      }
            #    }
            #   }
            # }
            
            ##if not 'resource' in self:
            ##    self['resource'] = NestedDefaultDict()
            self['resource'][block._labels[0]][block._labels[1]] = block
            
        elif isinstance(block, Resource):
            # Covers only subclasses of Resource because of 'if type()...' above. 
            #
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

            ##if not 'resource' in self:
            ##    self['resource'] = NestedDefaultDict()
            self['resource'][block.__class__.__name__][block._labels[0]] = block
            
        elif type(block) == Provider:
            #
            # {
            #   "resource": {}, 
            #     "provider": {
            #       "openstack": {                 <== block._labels[0]
            #          "user_name": "admin", 
            #          "tenant_name": "admin", 
            #          "password": "pwd", 
            #          "auth_url": "http://myauthurl:5000/v2.0", 
            #          "region": "RegionOne"
            #       }
            #     }
            #   }
            # }
            #
            self['provider'][block._labels[0]] = block
            
        elif isinstance(block, Provider):
            #
            # {
            #   "resource": {}, 
            #     "provider": {
            #       "openstack": {                 <== block.__class__.__name__
            #          "user_name": "admin", 
            #          "tenant_name": "admin", 
            #          "password": "pwd", 
            #          "auth_url": "http://myauthurl:5000/v2.0", 
            #          "region": "RegionOne"
            #       }
            #     }
            #   }
            # }
            #
            self['provider'][block.__class__.__name__] = block

        else:
            # TODO: Create test for trying to add a non-Terraform class to a terrascript instance,
            raise ValueError('An instance of %s cannot be added to instances of %s' % block.__class__.__name__, self.__class__.__name__)
        
        return self
            
    add = __add__

    def dump(self):
        """The `dump()` method is kept for backwards compatibilty
           as the `__str__()` method returns the JSON representation.

        """
        
        warnings.warn('The Terrascript.dump() method will be removed in the future. Use str(...) instead.',
                      category=DeprecationWarning)

        return str(self)

    def validate(self):
        """Validate a Terraform configuration."""
        
        warnings.warn('The Terrascript.validate() method will be removed in the future. Use the Terraform CLI instead.',
                      category=DeprecationWarning)
        
        result, _ = _validate(self)

        return result
    
    
class Resource(Block):
    """Base class for actual resource classes.
    
       This class can be instantiated directly to define Terraform resources
       for which no subclass of `Resource` exists in Terrascript. 
    
       Derived classes must be named *exactly* like the
       Terraform resource they represent.
          
       https://www.terraform.io/docs/configuration/resources.html
    """
    
    def __init__(self, *labels, **args):
        if type(self) == Resource:
            if len(labels) != 2:
                raise TypeError('%s takes exactly two arguments (%d given)' % 
                                (self.__class__.__name__, len(labels)))
        else:
            if len(labels) != 1:
                raise TypeError('%s takes exactly one argument (%d given)' % 
                                (self.__class__.__name__, len(labels)))
        super(Resource, self).__init__(*labels, **args)


class Provider(Block): 
    """Class for providers.
    
       Currently there are no subclasses of `Provider` and the class
       must be used directly.
       
       https://www.terraform.io/docs/configuration/providers.html
       
    """
    
    def __init__(self, label, **args):
        super(Provider, self).__init__(label, **args)


__all__ = ['Block', 'Terrascript', 'Resource', 'Provider']
