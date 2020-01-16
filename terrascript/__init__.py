"""
terrascript/__init__.py

Base classes and functions that are used everywhere else in
this project.

"""

import logging
import warnings
import json

__author__ = 'Markus Juenemann <markus@juenemann.net>'
__version__ = '0.8.0'
__license__ = 'BSD 2-clause "Simplified" License'

INDENT = 2
"""JSON indentation level."""

DEBUG = False
"""Set to enable some debugging."""

LOG = logging.getLogger(__name__)

PROVIDER_KEY = 'provider'
RESOURCE_KEY = 'resource'
MODULE_KEY = 'module'
VARIABLE_KEY = 'variable'
OUTPUT_KEY = 'output'
LOCALS_KEY = 'locals'
DATA_KEY = 'data'
TERRAFORM_KEY = 'terraform'


class Attribute(str):
    """An `Attribute` handles access to not yet known attributes.

       This called by `Block.__getattr__` to deal with

       In the example below the ``aws_instance`` does not have attributes
       ``.server`` and in turn ``.server.private_ip``. To prevent Python
       from raising an `AttributeError` the `Attribute.__getattr__()` method
       creates a new string by appending the attribute name.

       Python:

            config = terrascript.Terrascript()
            config += terrascript.aws.aws(version='~> 2.0', region='us-east-1')
            aws_instance = terrascript.aws.r.aws_instance('web', ...)
            config += aws_instance
            config += terrascript.Output('instance_ip_addr',
                                          value=aws_instance.server.private_ip)
                                                            ^^^^^^^^^^^^^^^^^^

        JSON:

    """

    def __getattr__(self, name):
        return Attribute('{}.{}'.format(self, name))


class Block(dict):
    """A `Block` is a dictionary-like container for other content.

    """

    def __init__(self, **kwargs):

        # Convert instances of Resource, Variable, Data, ... into
        # their correct reference instead of inserting the actual
        # dictionary.
        #
        # Resource ->
        # Variable -> "var.name"
        # TODO: Add others?
        #
        for k, v in kwargs.items():
            if isinstance(v, Variable):
                kwargs[k] = 'var.{}'.format(v._name)

        super().update(kwargs)

    def __getattr__(self, attr):
        """Special handling for accessing attributes,

           If ``Block.attr`` does not exist, try to return Block[attr]. If that
           does not exists either, return `attr` as a string, prefixed
           by the name (and type) of the Block that is referenced.

           This is for example necessary for referencing an attribute of a
           Terraform resource which only becomes available after the resource
           has been created.

           Example:

               instance = terrascript.resources.aws_instance("server", ...)
               output = terrascript.Output("instance_ip_addr",
                                           value=instance.private_ip)
                                                        ^^^^^^^^^^
           Where ``instance.private_ip`` does not (yet) exist.

        """

        # Try to return the entry in the dictionary. Otherwise return a string
        # which must be formatted differently depending on what is referenced.
        #
        if attr in self:
            return self[attr]
        else:
            if isinstance(self, Resource):
                return Attribute('{}.{}.{}'.format(self.__class__.__name__, self._name, attr))
            elif isinstance(self, Locals):
                return Attribute('local.{}'.format(attr))
            elif isinstance(self, Data):
                # data.google_compute_image.NAME.ATTR
                return Attribute('data.{}.{}.{}'.format(self.__class__.__name__, self._name, attr))
            else:
                raise AttributeError(attr)


class NamedBlock(Block):
    def __init__(self, _name, **kwargs):
        self._name = _name
        super().__init__(**kwargs)
        # TODO: Can this be done similar to NamedSubBlock?


class NamedSubBlock(Block):
    """NamedSubBlocks are similar to NamedBlocks except that the `name`
       is the key to a nested dictionary contain `kwargs`. NamedSubBlocks
       are not added to the top-level Terrascript structure but are
       arguments to another block. The backend argument to a Terraform
       block is a good example. 

       :param name: Name of the block, e.g. 'consul'.

    """

    def __init__(self, name, **kwargs):
        super().__init__()
        self[name] = kwargs


class Terrascript(dict):
    """Top-level container for Terraform configurations.

       :param *objects: Optional list of Terrascript data sources, resources,

    """

    def __init__(self, *objects):
        super().__init__()

        for object in objects:
            self += object


    def __str__(self):
        return json.dumps(self, indent=INDENT)

    def __add__(self, block):
        """Add a block to the configuration using the ``+`` syntax."""

        #
        # Resource
        #
        if isinstance(block, Resource):
            # self['resource']
            if RESOURCE_KEY not in self:
                self[RESOURCE_KEY] = {}
            # self['resource'][RESOURCE]
            if block.__class__.__name__ not in self[RESOURCE_KEY]:
                self[RESOURCE_KEY][block.__class__.__name__] = {}
            # self['resource'][RESOURCE][NAME] = {...}
            self[RESOURCE_KEY][block.__class__.__name__][block._name] = block
        #
        # Data
        #
        elif isinstance(block, Data):
            # self['data']
            if DATA_KEY not in self:
                self[DATA_KEY] = {}
            # self['data'][DATASOURCE]
            if block.__class__.__name__ not in self[DATA_KEY]:
                self[DATA_KEY][block.__class__.__name__] = {}
            # self['data'][DATASOURCE][NAME] = {...}
            self[DATA_KEY][block.__class__.__name__][block._name] = block
        #
        # Module
        #
        elif isinstance(block, Module):
            # self['module']
            if MODULE_KEY not in self:
                self[MODULE_KEY] = {}
            # self['module'][NAME] = {}
            self[MODULE_KEY][block._name] = block
        #
        # Provider
        #
        elif isinstance(block, Provider):
            # self['provider']
            if PROVIDER_KEY not in self:
                self[PROVIDER_KEY] = {}
            # self['provider'][PROVIDER]
            if block.__class__.__name__ not in self[PROVIDER_KEY]:
                self[PROVIDER_KEY][block.__class__.__name__] = []
            # self['provider'][PROVIDER] = [{...}, ...]
            self[PROVIDER_KEY][block.__class__.__name__].append(block)
        #
        # Variable
        #
        elif isinstance(block, Variable):
            # self['variable']
            if VARIABLE_KEY not in self:
                self[VARIABLE_KEY] = Block()
            # self['variable'][NAME]
            self[VARIABLE_KEY][block._name] = block
        #
        # Output
        #
        elif isinstance(block, Output):
            # self['output']
            if OUTPUT_KEY not in self:
                self[OUTPUT_KEY] = Block()
            # self['output'][NAME]
            self[OUTPUT_KEY][block._name] = block
        #
        # Locals
        #
        elif isinstance(block, Locals):
            # self['locals']
            if LOCALS_KEY not in self:
                self[LOCALS_KEY] = Block()
            # self['locals'][NAME]
            self[LOCALS_KEY].update(block)
        #
        # Terraform
        #
        elif isinstance(block, Terraform):
            self[TERRAFORM_KEY] = block
        #
        # else
        #
        else:
            raise TypeError('A {} cannot be added to the configuration'.format(
                block.__class__.__name__))

        return self

    def add(self, object):
        """Add to the configuration using the ``+`` syntax."""

        self += object
        return object    # for backwards compatability!

# Top-level blocks ----------------------------------------

class Resource(NamedBlock):
    """Terraform resource block."""
    pass


class Data(NamedBlock):
    """Terraform data source block."""
    pass


class Provider(Block):
    """Terraform provider

       HCL:

            provider "aws" {
                region = "us-east-1"
                version = "u~> 2.0"
            }

       JSON:

            "provider": {
                "aws": [
                    {
                        "region": "us-east-1",
                        "version": "~> 2.0"
                    }
                ]
            }

    """
    pass


class Variable(NamedBlock):
    pass


class Module(NamedBlock):
    """Terraform child module call.

       https://www.terraform.io/docs/configuration/modules.html

    """
    pass


class Output(NamedBlock):
    pass


# Top-level blocks ----------------------------------------

class Provisioner(dict):
    """A provisioner is a nested dictionary.

       The `name` argument must be a valid Terraform provisioner.

       >>> p = terrascript.Provisioner("local-exec", command="echo 'Hello World'")
       >>> print(p)
       {'local-exec': {'command': "echo 'Hello World"}}
    
       https://www.terraform.io/docs/provisioners/index.html

    """

    def __init__(self, name, **kwargs):
        self[name] = kwargs

class Connection(Block):
    pass


class Backend(NamedSubBlock):
    pass


class Terraform(Block):
    pass


class Locals(Block):
    # Not working, use Python variables instead.
    pass


class Function(Block):
    pass


# Lower case classes for backwards compatability with the exception of 'locals'
# and the classes that are subclassed in modules (resource, data, provider).
variable = Variable
module = Module
output = Output
provisioner = Provisioner
connection = Connection
backend = Backend
terraform = Terraform
function = Function

__all__ = ['Terrascript', 'Block', 'Resource', 'Provider', 'Datasource',
           'Variable', 'Module', 'Output', 'Provisioner', 'Backend',
           'Terraform', 'Locals', 'Function', 'resource', 'data', 'variable',
           'provider', 'module', 'output', 'provisioner', 'connection',
           'backend', 'terraform', 'function']
