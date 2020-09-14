Examples
--------
More examples can be found in in `Terrascripts examples/`_ directory.

.. _`Terrascripts examples/`: https://github.com/mjuenema/python-terrascript/tree/develop/examples

AWS
~~~

VPCs
....

This example has been copied from the `Terraform documentation for the AWS Provider`_.

.. _`Terraform documentation for the AWS Provider`: https://www.terraform.io/docs/providers/aws/index.html

Terraform HCL code:

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

Python code:

.. literalinclude:: examples/aws/vpc/basic.py

JSON output:

.. literalinclude:: examples/aws/vpc/basic.tf.json

Provider Endpoints
..................

Terraform HCL code:

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

Python code:

.. literalinclude:: examples/aws/provider/endpoints.py

JSON output:

.. literalinclude:: examples/aws/provider/endpoints.tf.json
