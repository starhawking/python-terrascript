Quickstart
----------

The following samples shows Terraform's native HCL format and the
Terrascript equivalent.

.. code-block:: none

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
    
   
The ``terrascript.Config`` class is the top-level container
for configurations. The provider and resource objects are then simply added 
to the configuration. Their names are the same as in the HCL language.

.. code-block:: python
    
   config = terrascript.Config()
   config += terrascript.aws.aws(profile='default', region="us-east-1")
   config += terrascript.aws.r.aws_instance('example', ami='ami-2757f631', instance_type='t2.micro')
                                
The content of ``config`` is actually just a Python dictionary with some 
additional smarts.

.. code-block:: python

   assert isinstance(config, dict) is True

Finally ``config`` has to be converted into JSON which can be achieved in three
different ways.

Option 1: Simply use the ``str()`` representation to print or convert to JSON.

.. code-block:: python

   print(config)
   # or
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
   
Whichever method you chose, the output will be the following JSON code.

.. code-block:: json

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
             "ami": "ami-2757f631",
             "instance_type": "t2.micro"
          }
        }
      }
    }
    
The generated JSON file is valid input for Terraform.

.. code-block:: console

    $ terraform init
    
    Initializing the backend...
    
    Initializing provider plugins...
    - Checking for available provider plugins...
    - Downloading plugin for provider "aws" (terraform-providers/aws) 2.25.0...
    
    The following providers do not have any version constraints in configuration,
    so the latest version was installed.
    
    To prevent automatic upgrades to new major versions that may contain breaking
    changes, it is recommended to add version = "..." constraints to the
    corresponding provider blocks in configuration, with the constraint strings
    suggested below.
    
    * provider.aws: version = "~> 2.25"
    
    Terraform has been successfully initialized!
    
    $ terraform validate
    Success! The configuration is valid.
