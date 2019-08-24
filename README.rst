python-terrascript
------------------

Python-Terrascript Terrascript is a Python package for generating Terraform 
configurations in JSON format.

This is the ``develop`` branch of Terrascript which is currently 
undergoing a major rewrite and is unlikely to be useful at this stage.

Creating Terraform through a Python script offers a degree of flexibility 
superior to writing Terraform configurations by hand.

* Control structures like ``if``/``else``, ``for``/``continue``/``break`` or ``try``/``except``/``finally``.
* More string methods.
* Python functions may be used as an alternative to Terraform Modules.
* Access to the Python Standard Library and third-party packages.

.. _Terraform: https://www.terraform.io 

Compatibility
~~~~~~~~~~~~~

`Terraform 0.12` introduced some changes to how it deals with configuration 
files in JSON format. This is reflected in Terrascript by currently having
separate releases for Terraform 0.12 and Terraform 0.11. Earlier releases of 
Terraform are not supported. 

.. _`Terraform 0.12`: https://www.hashicorp.com/blog/announcing-terraform-0-12  

========== ============ ==================================================================
Terraform  Terrascript  Notes                                                             
========== ============ ================================================================== 
0.12.x     0.8.x        Terrascript 0.8 will be an (almost) complete rewrite                   
0.12.x     0.7.x        Initial support for Terraform 0.12. Will be replaced by 0.8 later
0.11.x     0.6.x        Last releases to support Terraform 0.11 and earlier               
========== ============ ==================================================================

Terrascript supports Python 3.3 and later.

A first example
~~~~~~~~~~~~~~~

The following example has been taken from the official Terraform documentation 
for the `AWS Provider`_ and then converted into a Python script that generates 
the equivalent configuration in JSON.

.. _`AWS Provider`: https://www.terraform.io/docs/providers/aws/index.html 

The original Terraform HCL format. 

::
    
    provider "aws" {
      version = "~> 2.0"
      region  = "us-east-1"
    }
    
    # Create a VPC
    resource "aws_vpc" "example" {
      cidr_block = "10.0.0.0/16"
    }

The Terrascript code would look like this. 

::

    import terrascript
    import terrascript.aws
    import terrascript.aws.r

    config = terrascript.Terrascript()

    config += terrascript.aws.aws(version='~> 2.0', region='us-east-1')
    config += terrascript.aws.r.aws_vpc('example', cidr_block='10.0.0.0/16')
    
    with open('config.tf.json', wt') as fp:
        fp.write(str(config))

The content of ``config.tf.json`` will be this which is equivalent to the
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

.. _Documentation: https://python-terrascript.readthedocs.io/en/index.html
.. _Github: https://github.com/mjuenema/python-terrascript
