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
 

Looking for more contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IF you feel that this project is useful to you, please consider contributing some of your time towards improving it!
For more details on contributions, please have a look at CONTRIBUTORS.md and DEVELOPMENT.md.

About 
~~~~~

Python-Terrascript is a Python package for generating Terraform configurations in JSON format.

Creating Terraform through a Python script offers a degree of flexibility 
superior to writing Terraform configurations by hand.

* Control structures like ``if``/``else``, ``for``/``continue``/``break`` or ``try``/``except``/``finally``.
* More string methods.
* Python functions may be used as an alternative to Terraform_ Modules.
* Access to the Python Standard Library and third-party packages.

The file PROVIDERS.md_ lists all currently supported Terraform providers.

.. _PROVIDERS.md: _PROVIDERS.md 

Installing Terrascript
~~~~~~~~~~~~~~~~~~~~~~

Terrascript is available from the Python Package Repository PyPi_ or
alternatively from its Github_ repository.

.. _PyPi: https://pypi.org/project/terrascript/#history
.. _Github: https://github.com/mjuenema/python-terrascript


Installing Terrascript from PyPi
..................

It is easiest to install Terrascript directly from the Python Package Index.

.. code-block:: console

   $ python3 -m pip install terrascript

Installing Terrascript from Github
...................................

Terrascript can also be installed from its Github_ repository.

.. code-block:: console

   $ git clone https://github.com/mjuenema/python-terrascript.git
   $ cd python-terrascript/
   $ git fetch
   $ git fetch --tags
   
The ``master`` branch should be identical to the version on PyPi.

.. code-block:: console

   $ git checkout master
   $ python3 setup.py install

The ``develop`` branch includes the latest changes but may not always
be in a stable state. Do not use the ``develop`` branch unless you want 
to submit a merge request on github.

.. code-block:: console

   $ git checkout develop
   $ python3 setup.py install

Compatibility
~~~~~~~~~~~~~

Terraform releases
..................

`Terraform 0.13`_ added the `required providers` block together with tighter
integration with the `Terraform Provider Registry`. Terrascript 0.10.x
reflects this change and is *not backwards compatible* with earlier Terraform
releases.   

`Terraform 0.12`_ introduced some changes to how it deals with configuration 
files in JSON format. This is reflected in Terrascript by currently having
separate releases for Terraform 0.12 and Terraform 0.11. Earlier releases of 
Terraform are not supported. 

.. _`Terraform 0.12`: https://www.hashicorp.com/blog/announcing-terraform-0-12
.. _`Terraform 0.13`: https://www.hashicorp.com/blog/announcing-hashicorp-terraform-0-13  

========== ============ ============================================================================================
Terraform  Terrascript  Notes
========== ============ ============================================================================================
0.13.x     0.10.x       Introduced namespaces, many more providers, suppports Terraform 0.13 only 
0.13.x     0.9.x        Cleanup efforts and bug fixes, dropping support for Python <3.6, supporting Terraform 0.13.x
0.12.x     0.8.x        Terrascript 0.8 are a (almost) complete rewrite
0.12.x     0.7.x        Never released
0.11.x     0.6.x        Last releases to support Terraform 0.11 and earlier
========== ============ ============================================================================================

Terrascript supports Python 3.6 and later.

Module layout
.............

Python-Terrascript release 0.8.0 changed the location of modules. 
Providers, resources and data sources are now all available through just
three modules.

::

    import terrascript
    import terrascript.provider     # aws, google, ...
    import terrascript.resource     # aws_instance, google_compute_instance, ...
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
    import terrascript.provider as provider
    import terrascript.resource as resource

    config = terrascript.Terrascript()

    config += provider.aws(version='~> 2.0', region='us-east-1')
    config += resource.aws_vpc('example', cidr_block='10.0.0.0/16')
    
    with open('config.tf.json', 'wt') as fp:
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
**This is a deliberate design decision and is explained in the** `Frequently Asked Questions (FAQ) <https://python-terrascript.readthedocs.io/en/develop/faq.html>`_

.. _Frequently Asked Questions (FAQ): https://python-terrascript.readthedocs.io/en/develop/faq.html

Links
~~~~~

* Terraform_ for Terraform.
* Documentation_ for Python-Terrascript.
* Github_ page of Python-Terrascript.
* `Terraform JSON`_ syntax.

.. _Terraform: https://www.terraform.io 
.. _Documentation: https://python-terrascript.readthedocs.io/en/develop/
.. _Github: https://github.com/mjuenema/python-terrascript
.. _`Terraform JSON`: https://www.terraform.io/docs/configuration/syntax-json.html
