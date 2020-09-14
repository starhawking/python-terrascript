Tutorial
---------

This section explains the different Terrascript Python classes that can
be used to generate a Terraform configuration.

Since release 0.8.0 all Terrascript classes are available by importing
just four modules.

.. code-block:: python

    import terrascript
    import terrascript.provider
    import terrascript.resource
    import terrascript.data

.. note:: The old layout, e.g. ``import terarscript.aws.r`` is still available
          for backward compatibility but its use is discouraged. 

Provider
~~~~~~~~

Providers_ can be found in the ``terrascript.provider`` module, with one class
for each provider. Terrascript supports most Terraform providers. The full list 
can be found in `List of Providers`_.


**HCL**

.. literalinclude:: tutorials/provider1.tf

**Python**

.. literalinclude:: tutorials/provider1.py

**JSON**

.. literalinclude:: tutorials/provider1/provider1.tf.json

.. _Providers: https://www.terraform.io/docs/providers/index.html
.. _`List of Providers`: https://www.terraform.io/docs/providers/index.html

Resource
~~~~~~~~

Resources can be found in the ``terrascript.resource`` module. The example below shows
the original HCL syntax for creating an AWS S3 bucket and the equivalent Python code. 

**HCL**

.. literalinclude:: tutorials/resource1.tf

**Python**

And here is the same as a Python script. The first argument to ``terrascript.resource.aws_s3_bucket()``
is the Terraform label under which it can be referenced later. Note how the ``tags`` is a dictionary
as in the HCL syntax.

.. literalinclude:: tutorials/resource1.py

**JSON**

.. literalinclude:: tutorials/resource1/resource1.tf.json

Data Source
~~~~~~~~~~~

Data Sources are located in the ``terrascript.data`` module. The example creates a Google 
Compute Instance based on the Debian-9 image. First the Terrascript HCL syntax.

.. literalinclude:: tutorials/data1.tf

And the same as Python code. 

.. literalinclude:: tutorials/data1.py

The example above is mostly a one-to-one adaptation of the HCL syntax. Let's make some changes
to show how generating Terraform configurations through Python-Terrascript may help.

* Define the Google Compute Image family and Google Compute Instance machine type at the beginning 
  of the script so they are easier to change.
* Reference an instance of the Python-Terrascript class ``terrascript.data.google_compute_image()``
  as the boot disk image.
                                          
.. literalinclude:: tutorials/data2.py
   :emphasize-lines: 1,2,17,26

Variable
~~~~~~~~

The ``terrascript.Variable`` class can be used to define variables that can be referenced
later. Python-Terrascript automatically takes care of converting a reference to a Python
variable into the correct Terraform JSON syntax.

**HCL**

.. literalinclude:: tutorials/variable1.tf

**Python**

.. literalinclude:: tutorials/variable1.py
   :emphasize-lines: 11,18

**JSON**

In the output the reference to the ``image_id`` has been converted from a reference to a 
Python variable ``ami=v`` to the correct Terraform JSON syntax of ``${var.image_id}``.

.. literalinclude:: tutorials/variable1/variable1.tf.json
   :emphasize-lines: 18

Output
~~~~~~

Output is implemented as the ``terrascript.Output`` class. 

**HCL**

.. literalinclude:: tutorials/output1.tf

**Python**

.. literalinclude:: tutorials/output1.py

**JSON**

.. literalinclude:: tutorials/output1/output1.tf.json

Module
~~~~~~

Calls to other Terraform modules are implemented through the ``terrascript.Module`` class. 

**HCL**

.. literalinclude:: tutorials/module1.tf

**Python**

.. literalinclude:: tutorials/module1.py

**JSON**

.. literalinclude:: tutorials/module1/module1.tf.json

Backend
~~~~~~~

**HCL**

.. literalinclude:: tutorials/backend1.tf

**Python**

.. literalinclude:: tutorials/backend1.py

**JSON**

.. literalinclude:: tutorials/backend1/backend1.tf.json

Connection
~~~~~~~~~~

Locals
~~~~~~

Terraform local values are not supported. Use Python variables instead. 

**Python**

.. literalinclude:: tutorials/locals1.py
   :emphasize-lines: 11,18

**JSON**

.. literalinclude:: tutorials/locals1/locals1.tf.json
   :emphasize-lines: 15-16

Provisioner
~~~~~~~~~~~

One or multiple provisioners can be added to a Terraform resource.
Multiple provisioners must be added as a Python list, a single provisioner
can be either on its own or inside a list.

The example adds one "create" and one "destroy" provisioner.

**Python**

.. literalinclude:: tutorials/provisioner1.py
   :emphasize-lines: 24,25

**JSON**

.. literalinclude:: tutorials/provisioner1/provisioner1.tf.json
   :emphasize-lines: 16,21
