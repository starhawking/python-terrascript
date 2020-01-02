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


class String(str):
    """A `String` handles access to not yet known attributes.

       This called by `Block.__getattr__` to deal with

       In the example below the ``aws_instance`` does not have attributes
       ``.server`` and in turn ``.server.private_ip``. To prevent Python
       from raising an `AttributeError` the `String.__getattr__()` method
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
        return String('{}.{}'.format(self, name))


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
        #
        for k, v in kwargs.items():
            if isinstance(v, Variable):
                kwargs[k] = 'var.{}'.format(v.name)

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

        # The ``Block.name`` attribute gets special treatment. Some blocks have
        # names, which are the sole top-level key of the dictionary.
        #
        # Resources: {'resource_name': { ... }  ==> 'resource_name'
        # Provider: {'project': 'myproject', region: 'us_central1'} ==> AttributeError.
        #
#         if attr == 'name':
#             keys = list(self.keys())
#             if len(keys) > 1:
#                 raise AttributeError('{} has no name'.format(self.__class__.__name__))
#             else:
#                 return keys[0]

        # Try to return the entry in the dictionary. Otherwise return a string
        # which must be formatted differently depending on what is referenced.
        #
        try:
            raise KeyError  # TODO: what is this raise KeyError doing here?
            return self[attr]
        except KeyError:
            if isinstance(self, Resource):
                return String('{}.{}.{}'.format(self.__class__.__name__, self.name, attr))
            elif isinstance(self, Locals):
                return String('local.{}'.format(attr))
            elif isinstance(self, Provider):
                return '+++provider+++'
            
class NamedBlock(Block):
    def __init__(self, name, **kwargs):
        self._name = name
        super().__init__(**kwargs)


class Terrascript(dict):
    """Top-level container for Terraform configurations.

       :param *args: Optional list of Terrascript data sources, resources,

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
            #self[RESOURCE_KEY][block.__class__.__name__].update(block)
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
            #self[DATA_KEY][block.__class__.__name__].update(block)
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
            #self[VARIABLE_KEY].update(block)
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
            self[LOCALS_KEY][block._name] = block
        #
        # Input
        #
        # TODO: Input
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


class Resource(NamedBlock):
    """Terraform resource block."""
    pass

#     def __init__(self, name, **kwargs):
#         super().__init__()
#         self[name] = Block(**kwargs)


class Data(NamedBlock):
    """Terraform data source block."""
    pass

#     def __init__(self, name, **kwargs):
#         super().__init__()
#         self[name] = Block(**kwargs)


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

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)


class Variable(NamedBlock):
    pass
#     def __init__(self, name, **kwargs):
#         super().__init__()
#         self[name] = Block(**kwargs)


class Module(NamedBlock):
    """Terraform child module call.

       https://www.terraform.io/docs/configuration/modules.html

    """
    pass

#     def __init__(self, name, **kwargs):
#         super().__init__()
#         self[name] = Block(**kwargs)


class Output(NamedBlock):
    pass
#     def __init__(self, name, **kwargs):
#         super().__init__()
#         self[name] = Block(**kwargs)


class Provisioner(Block):
    """Provisioner block.

            resource "aws_instance" "web" {
                # ...

                provisioner "local-exec" {
                    command = "echo ${self.private_ip} > file.txt"
                }
            }

       :param name: The name of the provisioner, e.g. ``file``, ``local-exec``, ``chef``.
       :param **kwargs: The arguments are provisioner dependent.

    """
    pass

#     def __init__(self, name, **kwargs):
#         super().__init__()
#         self[name] = Block(**kwargs)


class Connection(Block):
    pass


class Backend(Block):
    pass


class Terraform(Block):
    pass


class Locals(Block):
    pass
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)


class Function(Block):
    pass


# Lower case classes for backwards will be deprecated in the future(???)

class module(Module):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class data(Data):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class resource(Resource):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class variable(Variable):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class provider(Provider):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class output(Output):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class provisioner(Provisioner):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class connection(Connection):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class backend(Backend):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class terraform(Terraform):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)

class function(Function):
    def   init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


__all__ = ['Terrascript', 'Block', 'Resource', 'Provider', 'Datasource',
           'Variable', 'Module', 'Output', 'Provisioner', 'Backend',
           'Terraform', 'Locals', 'Function']
