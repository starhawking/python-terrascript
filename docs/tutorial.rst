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
can be found in the appendices.

**HCL**

.. literalinclude:: examples/tutorial_provider1.tf

**Python**

.. literalinclude:: examples/tutorial_provider1.py

**JSON**

.. literalinclude:: examples/tutorial_provider1/tutorial_provider1.tf.json

.. _Providers: https://www.terraform.io/docs/providers/index.html

Resource
~~~~~~~~

Resources can be found in the ``terrascript.resource`` module. The example below shows
the original HCL syntax for creating an AWS S3 bucket and the equivalent Python code. 

**HCL**

.. literalinclude:: examples/tutorial_resource1.tf

**Python**

And here is the same as a Python script. The first argument to ``terrascript.resource.aws_s3_bucket()``
is the Terraform label under which it can be referenced later. Note how the ``tags`` is a dictionary
as in the HCL syntax.

.. literalinclude:: examples/tutorial_resource1.py

**JSON**

.. literalinclude:: examples/tutorial_resource1/tutorial_resource1.tf.json

Data Source
~~~~~~~~~~~

Data Sources are located in the ``terrascript.data`` module. The example creates a Google 
Compute Instance based on the Debian-9 image. First the Terrascript HCL syntax.

.. literalinclude:: examples/tutorial_data1.tf

And the same as Python code. 

.. literalinclude:: examples/tutorial_data1.py

The example above is mostly a one-to-one adaptation of the HCL syntax. Let's make some changes
to show how generating Terraform configurations through Python-Terrascript may help.

* Define the Google Compute Image family and Google Compute Instance machine type at the beginning 
  of the script so they are easier to change.
* Reference an instance of the Python-Terrascript class ``terrascript.data.google_compute_image()``
  as the boot disk image.
                                          
.. literalinclude:: examples/tutorial_data2.py
   :emphasize-lines: 1,2,16,22,26

Variable
~~~~~~~~

The ``terrascript.Variable`` class can be used to define variables that can be referenced
later. Python-Terrascript automatically takes care of converting a reference to a Python
variable into the correct Terraform JSON syntax.

**HCL**

.. literalinclude:: examples/tutorial_variable1.tf

**Python**

.. literalinclude:: examples/tutorial_variable1.py
   :emphasize-lines: 11,12,17

**JSON**

In the output the reference to the ``image_id`` has been converted from a reference to a 
Python variable ``ami=v`` to the correct Terraform JSON syntax of ``${var.image_id}``.

.. literalinclude:: examples/tutorial_variable1/tutorial_variable1.tf.json
   :emphasize-lines: 18

Output
~~~~~~

Output is implemented as the ``terrascript.Output`` class. 

**HCL**

.. literalinclude:: examples/tutorial_output1.tf

**Python**

.. literalinclude:: examples/tutorial_output1.py

**JSON**

.. literalinclude:: examples/tutorial_output1/tutorial_output1.tf.json
   :emphasize-lines: 18

Module
~~~~~~

Calls to other Terraform modules are implemented through the ``terrascript.Module`` class. 

**HCL**

.. literalinclude:: examples/tutorial_module1.tf

**Python**

.. literalinclude:: examples/tutorial_module1.py

**JSON**

.. literalinclude:: examples/tutorial_module1/tutorial_module1.tf.json

Backend
~~~~~~~

**HCL**

.. literalinclude:: examples/tutorial_backend1.tf

**Python**

.. literalinclude:: examples/tutorial_backend1.py

**JSON**

.. literalinclude:: examples/tutorial_module1/tutorial_backend1.tf.json

Connection
~~~~~~~~~~

Locals
~~~~~~

Terraform local values are not supported. Use Python variables instead. 

**Python**

.. literalinclude:: examples/tutorial_locals1.py
   :emphasize-lines: 11,12,17

**JSON**

.. literalinclude:: examples/tutorial_locals1/tutorial_locals1.tf.json
   :emphasize-lines: 14,15,16

Provisioner
~~~~~~~~~~~

One or multiple provisioners can be added to a Terraform resource.
Multiple provisioners must be added as a Python list, a single provisioner
can be either on its own or inside a list. The example adds one "create"
and one "destroy" provisioner.

**Python**

.. literalinclude:: examples/tutorial_provisioner1.py
   :emphasize-lines: 10,11,15

**JSON**

.. literalinclude:: examples/tutorial_provisioner1/tutorial_provisioner1.tf.json
   

