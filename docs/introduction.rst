Terrascript
===========

Terrascript is a Python_ package for creating Terraform_ configurations in JSON_.

Creating Terraform configurations this way gives one the power of the control and
data structures of the Python language which Terraform's native HCL_ format 
mostly lack. Furthermore access to the modules of the Python Standard Library 
or other third-party Python packages are further arguments for creaing Terraform
configurations through Python scripts.

Terrascript only supports Python 3.3+ and back-porting it to earlier versions of
Python is not planned.

.. _Python: https://www.python.org/
.. _Terraform: https://www.terraform.io/
.. _JSON: https://www.terraform.io/docs/configuration/syntax-json.html
.. _HCL: https://www.terraform.io/docs/configuration/index.html