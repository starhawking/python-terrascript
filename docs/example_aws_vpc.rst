Example 1: AWS VPC
~~~~~~~~~~~~~~~~~~

This example has been copied from the 
`Terraform documentation for the AWS Provider`_.

.. _`Terraform documentation for the AWS Provider`: https://www.terraform.io/docs/providers/aws/index.html

Terraform HCL.

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

Terrascript.

.. literalinclude:: ../tests/test_001.py
   :lines: 13-16
   :dedent: 4
   
JSON output.

.. literalinclude:: ../tests/configs/test_001.tf.json