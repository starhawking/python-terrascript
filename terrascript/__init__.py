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
        if attr == 'name':
            keys = list(self.keys())
            if len(keys) > 1:
                raise AttributeError('{} has no name'.format(self.__class__.__name__))
            else:
                return keys[0]

        # Try to return the entry in the dictionary. Otherwise return a string
        # which must be formatted differently depending on what is referenced.
        #
        try:
            raise KeyError
            return self[attr]
        except KeyError:
            if isinstance(self, Resource):
                return String('{}.{}.{}'.format(self.__class__.__name__, self.name, attr))
            elif isinstance(self, Locals):
                return String('local.{}'.format(attr))
            elif isinstance(self, Provider):
                return '+++provider+++'


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

    def __add__(self, object):
        """Add to the configuration using the ``+`` syntax."""

        #
        # Resource
        #
        if isinstance(object, Resource):
            if RESOURCE_KEY not in self:
                self[RESOURCE_KEY] = {}
            if object.__class__.__name__ not in self[RESOURCE_KEY]:
                self[RESOURCE_KEY][object.__class__.__name__] = {}
            self[RESOURCE_KEY][object.__class__.__name__].update(object)
        #
        # Data
        #
        elif isinstance(object, Data):
            if DATA_KEY not in self:
                self[DATA_KEY] = {}
            if object.__class__.__name__ not in self[DATA_KEY]:
                self[DATA_KEY][object.__class__.__name__] = {}
            self[DATA_KEY][object.__class__.__name__].update(object)
        #
        # Module
        #
        elif isinstance(object, Module):
            if MODULE_KEY not in self:
                self[MODULE_KEY] = {}
            self[MODULE_KEY].update(object)
        #
        # Provider
        #
        elif isinstance(object, Provider):
            if PROVIDER_KEY not in self:
                self[PROVIDER_KEY] = {}
            if object.__class__.__name__ not in self[PROVIDER_KEY]:
                self[PROVIDER_KEY][object.__class__.__name__] = []
            self[PROVIDER_KEY][object.__class__.__name__].append(object)
        #
        # Variable
        #
        elif isinstance(object, Variable):
            if VARIABLE_KEY not in self:
                self[VARIABLE_KEY] = Block()
            self[VARIABLE_KEY].update(object)
        #
        # Output
        #
        elif isinstance(object, Output):
            if OUTPUT_KEY not in self:
                self[OUTPUT_KEY] = Block()
            self[OUTPUT_KEY].update(object)
        #
        # Locals
        #
        elif isinstance(object, Locals):
            if LOCALS_KEY not in self:
                self[LOCALS_KEY] = Block()
            self[LOCALS_KEY].update(object)
        #
        # else
        #
        else:
            raise TypeError('A {} cannot be added to the configuration'.format(
                object.__class__.__name__))

        return self

    def add(self, object):
        """Add to the configuration using the ``+`` syntax."""

        self += object
        return object


class Resource(Block):
    """Terraform resource block."""

    def __init__(self, name, **kwargs):
        super().__init__()
        self[name] = Block(**kwargs)


class Data(Block):
    """Terraform data source block.

    """

    def __init__(self, name, **kwargs):
        super().__init__()
        self[name] = Block(**kwargs)


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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Variable(Block):
    def __init__(self, name, **kwargs):
        super().__init__()
        self[name] = Block(**kwargs)


class Module(Block):
    """Terraform child module call.

       https://www.terraform.io/docs/configuration/modules.html

    """

    def __init__(self, name, **kwargs):
        super().__init__()
        self[name] = Block(**kwargs)


class Output(Block):
    def __init__(self, name, **kwargs):
        super().__init__()
        self[name] = Block(**kwargs)


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

    def __init__(self, name, **kwargs):
        super().__init__()
        self[name] = Block(**kwargs)


class Connection(Block):
    pass


class Backend(Block):
    pass


class Terraform(Block):
    pass


class Locals(Block):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Function(Block):
    pass


# Lower case classes for backwards will be deprecated in the future(???)

class module(Module):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class data(Data):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class resource(Resource):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class variable(Variable):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class provider(Provider):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class output(Output):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class provisioner(Provisioner):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class connection(Connection):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class backend(Backend):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class terraform(Terraform):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class function(Function):
    def __init__(self, *args, **kwargs):
        warnings.warn("'{}' will be deprecated in the future, please use '{}' instead".format(
            self.__class__.__name__, self.__class__.__name__.title()), PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


# THREE_TIER_ITEMS = ['data', 'resource', 'provider']
# TWO_TIER_ITEMS = ['variable', 'module', 'output', 'provisioner']
# ONE_TIER_ITEMS = ['terraform', 'locals']
#
#
# class _Config(dict):
#     def __getitem__(self, key):
#         try:
#             return super(_Config, self).__getitem__(key)
#         except KeyError:
#             # Work-around for issue 3 as described in https://github.com/hashicorp/terraform/issues/13037:
#             # Make 'data' a list of a single dictionary.
#             if key == 'data':
#                 super(_Config, self).__setitem__(key, [defaultdict(dict)])
#             elif key in THREE_TIER_ITEMS:
#                 super(_Config, self).__setitem__(key, defaultdict(dict))
#             elif key in TWO_TIER_ITEMS:
#                 super(_Config, self).__setitem__(key, {})
#             elif key in ONE_TIER_ITEMS:
#                 super(_Config, self).__setitem__(key, {})
#             else:
#                 raise KeyError(key)
#
#         return super(_Config, self).__getitem__(key)
#
#
# class Terrascript(object):
#     """Top-level container for Terraform configurations."""
#
#     def __init__(self):
#
#         self.config = _Config()
#         self._item_list = []
#
#     def __add__(self, item):
#         # Does not add EMPTY values
#         clone = item._kwargs.copy()
#         for k in clone:
#             if item._kwargs[k] is None:
#                 del item._kwargs[k]
#
#         # Work-around for issue 3 as described in https://github.com/hashicorp/terraform/issues/13037:
#         # Make 'data' a list of a single dictionary.
#         if item._class == 'data':
#             self.config[item._class][0][item._type][item._name] = item._kwargs
#         elif item._class in THREE_TIER_ITEMS:
#             self.config[item._class][item._type][item._name] = item._kwargs
#         elif item._class in TWO_TIER_ITEMS:
#             self.config[item._class][item._name] = item._kwargs
#         elif item._class in ONE_TIER_ITEMS:
#             self.config[item._class] = item._kwargs
#         else:
#             raise KeyError(item)
#
#         if not isinstance(item, Terrascript):
#             if item in self._item_list:
#                 self._item_list.remove(item)
#             self._item_list.append(item)
#
#         return self
#
#     def add(self, item):
#         self.__add__(item)
#         return item
#
#     def update(self, terrascript2):
#         if isinstance(terrascript2, Terrascript):
#             for item in terrascript2._item_list:
#                 self.__add__(item)
#         else:
#             raise TypeError('{0} is not a Terrascript instance.'.format(
#                 type(terrascript2)))
#
#     def dump(self):
#         """Return the JSON representaion of config."""
#         import json
#
#         def _json_default(v):
#             # How to encode non-standard objects
#             if isinstance(v, provisioner):
#                 return {v._type: v.data}
#             elif isinstance(v, UserDict):
#                 return v.data
#             else:
#                 return str(v)
#
#         # Work on copy of _Config but with unused top-level elements removed.
#         #
#         config = {k: v for k,v in self.config.items() if v}
#         return json.dumps(config, indent=INDENT, sort_keys=SORT, default=_json_default)
#
#
#     def validate(self, delete=True):
#         """Validate a Terraform configuration."""
#         import tempfile
#         import subprocess
#
#         config = self.dump()
#         with tempfile.TemporaryDirectory() as tmpdir:
#             tmpfile = tempfile.NamedTemporaryFile(mode='w', dir=tmpdir, suffix='.tf.json', delete=delete)
#
#             tmpfile.write(self.dump())
#             tmpfile.flush()
#
#             # Download plugins
#             proc = subprocess.Popen(['terraform','init'], cwd=tmpdir,
#                                     stdout=subprocess.PIPE, stderr=None)
#             proc.communicate()
#             assert proc.returncode == 0
#
#             # Validate configuration
#             proc = subprocess.Popen(['terraform','validate','-check-variables=false'], cwd=tmpdir,
#                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             proc.communicate()
#
#             tmpfile.close()
#
#         return proc.returncode == 0
#
#
# class _base(object):
#     _class = None
#     """One of 'resource', 'data', 'module', etc."""
#
#     _type = None
#     """The resource type, e.g. 'aws_instance'."""
#
#     _name = None
#     """The name of this resource, e.g. 'my_ec2_instance'."""
#
#     def __init__(self, name_, **kwargs):
#         if not self._type:
#             self._type = self.__class__.__name__
#         self._name = name_
#         self._kwargs = kwargs
#
#
#     def __getattr__(self, name):
#         """References to attributes."""
#         if self._class == 'resource':
#             return '${{{}.{}.{}}}'.format(self._type, self._name, name)
#         elif self._class == 'module':
#             return '${{module.{}.{}}}'.format(self._name, name)
#         else:
#             return '${{{}.{}.{}.{}}}'.format(self._class, self._type, self._name, name)
#
#     def __getitem__(self, i):
#         if isinstance(i, int):
#             # "${var.NAME[i]}"
#             return '${{var.{}[{}]}}'.format(self._name, i)
#         else:
#             # "${var.NAME["i"]}"
#             return "${{var.{}[\"{}\"]}}".format(self._name, i)
#
#     def __repr__(self):
#         """References to objects."""
#         if self._class == 'variable':
#             """Interpolated reference to a variable, e.g. ``${var.http_port}``."""
#             return self.interpolated
#         else:
#             """Non-interpolated reference to a non-resource, e.g. ``module.http``."""
#             return self.fullname
#
#     @property
#     def interpolated(self):
#         """The object in interpolated syntax: ``${...}``."""
#         return '${{{}}}'.format(self.fullname)
#
#     @property
#     def fullname(self):
#         """The object's full name."""
#         if self._class == 'variable':
#             return 'var.{}'.format(self._name)
#         elif self._class == 'resource':
#             return '{}.{}'.format(self._type, self._name)
#         else:
#             return '{}.{}'.format(self._class, self._name)
#
#
# class _resource(_base):
#     """Base class for resources."""
#     _class = 'resource'
#
#
# class _data(_base):
#     """Base class for data sources."""
#     _class = 'data'
#
#     def __init__(self, obj_name, **kwargs):
#         super(_data, self).__init__(obj_name, **kwargs)
#
#
# class resource(_base):
#     """Class for creating a resource for which no convenience wrapper exists."""
#     _class = 'resource'
#
#     def __init__(self, type_, name, **kwargs):
#         self._type = type_
#         super(resource, self).__init__(name, **kwargs)
#
#
# class data(_base):
#     """Class for creating a data source for which no convenience wrapper exists."""
#     _class = 'data'
#
#     def __init__(self, type_, name, **kwargs):
#         self._type = type_
#         super(data, self).__init__(name, **kwargs)
#
#
# class module(_base):
#     _class = 'module'
#
#
# class variable(_base):
#     _class = 'variable'
#
#
# class output(_base):
#     _class = 'output'
#
#
# class provider(_base):
#     _class = 'provider'
#
#     def __init__(self, name, **kwargs):
#        alias = kwargs.get('alias', '__DEFAULT__')
#        self._type = name
#        super(provider, self).__init__(alias, **kwargs)
#
#
# class Locals(_base):
#     _class = 'locals'
#
#     def __init__(self, **kwargs):
#         super(Locals, self).__init__(None, **kwargs)
#
#
# class terraform(_base):
#     _class = 'terraform'
#     def __init__(self, **kwargs):
#         # Terraform does not have a name
#         super(terraform, self).__init__(None, **kwargs)
#
#
# class provisioner(UserDict):
#     def __init__(self, type_, **kwargs):
#        self._type = type_
#        self.data = kwargs
#
#
# class connection(UserDict):
#     def __init__(self,  **kwargs):
#         self.data = kwargs
#
#
# class backend(UserDict):
#     def __init__(self,  name, **kwargs):
#         self.data = {name: kwargs}
#
#
# class _function(object):
#     """Terraform function.
#
#        >>> function.lookup(map, key)
#        "${lookup(map, key)}"
#
#     """
#
#     class _function(object):
#         def __init__(self, name):
#             self.name = name
#
#         def format(self, arg):
#             """Format a function argument."""
#             if isinstance(arg, _base):
#                 return arg.fullname
#             elif isinstance(arg, str):
#                 return '"{}"'.format(arg)
#             else:
#                 return arg
#
#         def __call__(self, *args):
#             return '${{{}({})}}'.format(self.name, ','.join([self.format(arg) for arg in args]))
#
#     def __getattr__(self, name):
#         return self._function(name)
#
# f = fn = func = function = _function()
# """Shortcuts for `function()`."""
#
#
__all__ = ['Terrascript', 'Block', 'Resource', 'Provider', 'Datasource',
           'Variable', 'Module', 'Output', 'Provisioner', 'Backend',
           'Terraform', 'Locals', 'Function']
