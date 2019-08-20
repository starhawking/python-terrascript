"""
terrascript/__init__.py

Base classes and functions that are used elsewhere in
this project.

"""

import collections.abc
import json
import logging
import warnings
from abc import ABC, abstractmethod

from terrascript.reference import ReferenceMixin

__author__ = 'Markus Juenemann <markus@juenemann.net>'
__version__ = '0.7.1'
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
        super().__init__(NestedDefaultDict, *args, **kwargs)

    def __str__(self):
        return json.dumps(dict(self), indent=INDENT)


class Block(NestedDefaultDict):
    """A `Block` is a container for other content.
    
       See https://www.terraform.io/docs/configuration/syntax.html#blocks.
       
       TODO: Can we make this a NestedDefaultDict?
       
    """

    def __init__(self, *labels, **args):
        super().__init__()
        self._labels = labels
        self.update({
            key: self.convert_for_dependency(key, val)
            for key, val in args.items()
        })

    @staticmethod
    def convert_for_dependency(key, values):
        if key == "depends_on" and isinstance(values, list):
            return [repr(v) for v in values]
        else:
            return values


class TopLevelBlock(ABC, Block):
    @abstractmethod
    def add_to_terrascript(self, terrascript):
        ...


class Terrascript(Block):
    """Top-level container for Terraform configurations.
    
       It has neither labels nor arguments.
    """

    def __init__(self):
        super().__init__()

    def __add__(self, block):
        block.add_to_terrascript(self)
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


class Resource(ReferenceMixin, TopLevelBlock):
    """Base class for actual resource classes.
    
       This class can be instantiated directly to define Terraform resources
       for which no subclass of `Resource` exists in Terrascript. 
    
       Derived classes must be named *exactly* like the
       Terraform resource they represent.
          
       https://www.terraform.io/docs/configuration/resources.html
    """

    def __init__(self, *labels, **args):
        if len(labels) != 2:
            raise TypeError('%s takes exactly two arguments (%d given)' %
                            (self.__class__.__name__, len(labels)))
        super().__init__(*labels, **args)

    @property
    def ref_list(self):
        return self._labels

    def add_to_terrascript(self, terrascript):
        """
        {
         "resource": {
           "foobar":       {                 <== block._labels[0]
             "example": {                    <== block._labels[1]
               "instance_type": "t2.micro",
               "ami": "ami-abc123"
             }
           }
          }
        }
        """
        terrascript['resource'][self._labels[0]][self._labels[1]] = self


class Provider(TopLevelBlock):
    """Class for providers.
    
       Currently there are no subclasses of `Provider` and the class
       must be used directly.
       
       https://www.terraform.io/docs/configuration/providers.html
       
    """

    def __init__(self, label, **args):
        super().__init__(label, **args)

    def add_to_terrascript(self, terrascript):
        """
        {
          "resource": {},
            "provider": {
              "openstack": {                 <== block._labels[0]
                 "user_name": "admin",
                 "tenant_name": "admin",
                 "password": "pwd",
                 "auth_url": "http://myauthurl:5000/v2.0",
                 "region": "RegionOne"
              }
            }
          }
        }
        """
        terrascript['provider'][self._labels[0]] = self


class Terraform(TopLevelBlock):
    """Class for Terraform settings.

      https://www.terraform.io/docs/configuration/syntax-json.html#terraform-blocks
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def backend(self, name, **kwargs):
        """Helper method to add a backend config."""
        self['backend'][name] = kwargs
        return self

    def add_to_terrascript(self, terrascript):
        """
        {
          "terraform": {
            "required_version": ">= 0.12.0",
            "backend": {
              "s3": {
                "region": "us-west-2",
                "bucket": "acme-terraform-states"
              }
            }
          }
        }
        """
        terrascript['terraform'] = self


class Data(ReferenceMixin, TopLevelBlock):
    """Class for data.

      https://www.terraform.io/docs/configuration/syntax-json.html#resource-and-data-blocks
    """

    def __init__(self, *labels, **kwargs):
        if len(labels) != 2:
            raise TypeError('Data takes exactly two arguments (%d given)' % len(labels))
        super().__init__(*labels, **kwargs)

    @property
    def ref_list(self):
        return ('data',) + self._labels

    def add_to_terrascript(self, terrascript):
        """
        {
            "data": {
                "foo": {      <== block._labels[0]
                    "bar": {  <== block._labels[1]
                        "provider": "aws.foo"
                    }
                }
            }
        }
        """
        terrascript['data'][self._labels[0]][self._labels[1]] = self


class Output(TopLevelBlock):
    """Class for output.

    https://www.terraform.io/docs/configuration/syntax-json.html#output-blocks
    """

    def __init__(self, label, value):
        super().__init__(label, value=value)

    def add_to_terrascript(self, terrascript):
        """
        {
          "output": {
            "example": {        <== block._labels[0]
              "value": "${aws_instance.example}"
            }
          }
        }
        """
        terrascript['output'][self._labels[0]] = self


__all__ = ['Block', 'Terrascript', 'Resource', 'Provider', 'Terraform', 'Data', 'Output']
