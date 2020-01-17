python-terrascript
------------------

.. image:: https://img.shields.io/github/license/mjuenema/python-terrascript
   :target: https://opensource.org/licenses/BSD-2-Clause

.. image:: https://img.shields.io/travis/mjuenema/python-terrascript
   :target: https://www.travis-ci.org/mjuenema/python-terrascript/builds
   
.. image:: https://img.shields.io/pypi/v/terrascript
   :target: https://pypi.org/project/terrascript/
   
.. image:: https://img.shields.io/pypi/pyversions/terrascript
   :target: https://pypi.org/project/terrascript/
   
.. image:: https://img.shields.io/pypi/dm/terrascript
   :target: https://pypi.org/project/terrascript/
   
.. image:: https://img.shields.io/github/issues/mjuenema/python-terrascript
   :target: https://github.com/mjuenema/python-terrascript/issues
   
.. image:: https://img.shields.io/github/stars/mjuenema/python-terrascript
   :target: https://github.com/mjuenema/python-terrascript/stargazers
   
.. image:: https://img.shields.io/badge/zulip-join_chat-brightgreen.svg
   :target: https://python-terrascript.zulipchat.com/

Python-Terrascript is a Python package for generating Terraform 
configurations in JSON format.

Creating Terraform through a Python script offers a degree of flexibility 
superior to writing Terraform configurations by hand.

* Control structures like ``if``/``else``, ``for``/``continue``/``break`` or ``try``/``except``/``finally``.
* More string methods.
* Python functions may be used as an alternative to Terraform Modules.
* Access to the Python Standard Library and third-party packages.

.. _Terraform: https://www.terraform.io 

Compatibility
~~~~~~~~~~~~~

Terraform releases
..................

`Terraform 0.12` introduced some changes to how it deals with configuration 
files in JSON format. This is reflected in Terrascript by currently having
separate releases for Terraform 0.12 and Terraform 0.11. Earlier releases of 
Terraform are not supported. 

.. _`Terraform 0.12`: https://www.hashicorp.com/blog/announcing-terraform-0-12  

========== ============ ==================================================================
Terraform  Terrascript  Notes                                                             
========== ============ ================================================================== 
0.12.x     0.8.x        Terrascript 0.8 will be an (almost) complete rewrite                   
0.12.x     0.7.x        Never released
0.11.x     0.6.x        Last releases to support Terraform 0.11 and earlier               
========== ============ ==================================================================

Terrascript supports Python 3.3 and later.

Module layout
.............

Python-Terrascript release 0.8.0 changed the location of modules. 
Providers, resources and data sources are now all available through just
three modules.

::

    import terrascript
    import terrascript.providers    # aws, google, ...
    import terrascript.resources    # aws_instance, google_compute_instance, ...
    import terrascript.data         # aws_ami, google_compute_image, ...
    
The legacy layout is still available but should not be used for new projects.

:: 

    import terrascript
    import terrascript.aws          # aws
    import terrascript.aws.r        # aws_instance, ... 
    import terrascript.aws.d        # aws_ami, ...


A first example
~~~~~~~~~~~~~~~

The following example has been taken from the official Terraform documentation 
for the `AWS Provider`_ and then converted into a Python script that generates 
the equivalent configuration in JSON syntax.

.. _`AWS Provider`: https://www.terraform.io/docs/providers/aws/index.html 

The original Terraform HCL format. 

::
    
    provider "aws" {
      version = "~> 2.0"
      region  = "us-east-1"
    }
    
    resource "aws_vpc" "example" {
      cidr_block = "10.0.0.0/16"
    }

The Terrascript code would look like this. 

::

    import terrascript
    import terrascript.providers as providers
    import terrascript.resources as resources

    config = terrascript.Terrascript()

    config += providers.aws(version='~> 2.0', region='us-east-1')
    config += resources.aws_vpc('example', cidr_block='10.0.0.0/16')
    
    with open('config.tf.json', wt') as fp:
        fp.write(str(config))

The content of ``config.tf.json`` is shown below. It is equivalent to the
original HCL format.

::

    {
      "provider": {
        "aws": [
          {
            "version": "~> 2.0",
            "region": "us-east-1"
          }
        ]
      },
      "resource": {
        "aws_vpc": {
          "example": {
            "cidr_block": "10.0.0.0/16"
          }
        }
      }
    }

**Terrascript does not verify that the generated JSON code is a valid Terraform configuration.**
**This is a deliberate design decision and is explained in the Frequently Asked Questions (FAQ)**

Links
~~~~~

* Documentation_ for Python-Terrascript.
* Github_ page of Python-Terrascript.
* `Community Chat`_ on Zulip.
* `Terraform JSON`_ syntax.

.. _Documentation: https://python-terrascript.readthedocs.io/en/index.html
.. _Github: https://github.com/mjuenema/python-terrascript
.. _`Terraform JSON`: https://www.terraform.io/docs/configuration/syntax-json.html
.. _`Community Chat`: https://python-terrascript.zulipchat.com/
