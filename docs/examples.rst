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

.. literalinclude:: ../tests/test_001.py
   :lines: 9-16
   :dedent: 4
   
JSON output from ``print(config)``.

.. literalinclude:: ../tests/configs/test_001.tf.json

Terraform: Up & Running - Hello World
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Terraform HCL code.

.. literalinclude:: ../tests/test_TUAR_hello_world.py
   :lines: 7-21

Python code.

.. literalinclude:: ../tests/test_TUAR_hello_world.py
   :language: python
   :lines: 27-33
   :dedent: 4

JSON output.

.. literalinclude:: ../tests/configs/test_TUAR_hello_world.tf.json
   :language: json
   
Terraform: Up & Running - Why Terraform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Terraform HCL code.

.. literalinclude:: ../tests/test_TUAR_why_terraform.py
   :lines: 7-27


Python code.

.. literalinclude:: ../tests/test_TUAR_why_terraform.py
   :language: python
   :lines: 33-48
   :dedent: 4

JSON output.

.. literalinclude:: ../tests/configs/test_TUAR_why_terraform.tf.json
   :language: json