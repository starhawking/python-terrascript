Examples
--------

The examples are mostly extracted from Terrascript's `tests/`_ folder or
based on the book `"Terraform: Up & Running"`_ (1st and 2nd editions). 
written by Yevgenij Brikman.

.. _`tests/`: https://github.com/mjuenema/python-terrascript/tree/develop/tests
.. _`"Terraform: Up & Running"`: https://www.terraformupandrunning.com/

AWS VPC
~~~~~~~

This example has been copied from the `Terraform documentation for the AWS Provider`_.

.. _`Terraform documentation for the AWS Provider`: https://www.terraform.io/docs/providers/aws/index.html

Terraform HCL code.

.. code:: none

    # Configure the AWS Provider
    provider "aws" {
      version = "~> 2.0"
      region  = "us-east-1"
    }
    
    # Create a VPC
    resource "aws_vpc" "example" {
      cidr_block = "10.0.0.0/16"
    }

Python code.

.. literalinclude:: ../tests/test_example_001.py
   :lines: 9-15
   :dedent: 4
   
JSON output from ``print(config)``.

.. literalinclude:: ../tests/configs/test_001.tf.json

AWS Provider Endpoints
~~~~~~~~~~~~~~~~~~~~~~

Terraform HCL code.

.. code:: none

    # Configure AWS Provider with endpoints
    provider "aws" {
      version = "~> 2.0"
      region  = "us-east-1"
      endpoints = {
        dynamodb = "http://localhost:4569"
        s3 = "http://localhost:4572"
      }
    }

    # Create a VPC
    resource "aws_vpc" "example" {
      cidr_block = "10.0.0.0/16"
    }

Python code.

.. literalinclude:: ../tests/test_example_002.py
   :lines: 9-22
   :dedent: 4

JSON output from ``print(config)``.

.. literalinclude:: ../tests/configs/test_002.tf.json