Quickstart
----------

A basic example
~~~~~~~~~~~~~~~

The following samples shows Terraform's native HCL format and the
Terrascript equivalent. It is taken from Terraform Getting Started Guide.

.. code-block::

    provider "aws" {
      profile    = "default"
      region     = "us-east-1"
    }
    
    resource "aws_instance" "example" {
      ami           = "ami-2757f631"
      instance_type = "t2.micro"
    }
    
In Python, the first step is to import the required modules. In this example
this covers the main Terrascript module a the Amazon Web Services (AWS)
specific modules for the provider and resources like ``aws_instance``. 


.. code-block:: python

   import terrascript
   import terrascript.aws
   import terrascript.aws.r
    
   
In Terrascript the ``terrascript.Config`` class is the top-level container
for configurations. The provider and resource objects are then simply added 
to the configuration. Their names are the same as in the HCL language.

.. code-block:: python
    
   config = terrascript.Config()
   config += terrascript.aws.aws(profile='default', region="us-east-1")
   config += terrascript.aws.r.aws_instance('example', ami='ami-2757f631', 
                                            instance_type='t2.micro')
                                
The content of ``config`` is actually just a Python dictionary with some 
additional smarts that's for later.

Finally ``config`` has to be converted into JSON which can be achieved in three
different ways.

Option 1: Simply use the ``str()`` representation to print or convert to JSON.

.. code-block:: python

   print(config)
   
   cfg = str(config)
   
Option 2: Use the ``json`` module from the Python Standard Library but ensure 
that ``sort_keys`` is set to ``False``. ``indent`` can be set as preferred. 

.. code-block:: python

   import json
   
   cfg = json.dumps(config, indent=2, sort_keys=False).

Option 3: Use the ``.dump()`` method. This option has been retained for backward
compatibility and may be removed in the future.

.. code-block:: python

   cfg = config.dump()
   
Whichever method you chose, the output will be the following JSON code which is
a valid Terraform configuration.

.. code-block: json

    {
      "provider": {
        "aws": [
          {
            "profile": "default",
            "region": "us-east-1"
          }
        ]
      },
      "resource": {
        "aws_instance": {
          "example": {
             "ami": "ami-2757f631"
             "instance_type": "t2.micro"
          }
        }
      }
    }
   
Using the power of Python
~~~~~~~~~~~~~~~~~~~~~~~~~

The first example showed a one-to-one translation from HCL into a Python script
but didn't show off any advantages one gains when using the Terrascript
package. Below is an example that provide a glimpse why one 
would use Python scripts instead of writing Terraform configurations in HCL
by hand.

Read a list of AWS EC2 instances from a CSV file.

.. code-block:: 

    import terrascript
    import terrascript.aws
    import terrascript.aws.r
    
    import csv
    
    config = terrascript.Config()
    config += terrascript.aws.aws(profile='default', region="us-east-1")
    
    with open('instances.csv', 'rt') as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            config += terrascript.aws.r.aws_instance(row['name'], 
                                                     ami=row['ami'], 
                                                     instance_type=row['instance_type') 
                                                     
