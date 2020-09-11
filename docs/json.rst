Terraform JSON format
---------------------

The following sections show the JSON output Python-Terrascript generates for
the different Terraform elements.

Resource
~~~~~~~~

Resources are coded as nested dictionaries. The top-level key is the type
of the resource. The second-level key is the name of a resource instance.

Example:

* Two ``aws_instance`` resources named ``instance1`` and ``instance2``
* One ``aws_subnet`` resource named ``subnet1``.

.. code-block:: json
    
    {
      "resource": {
        "aws_instance": {
          "instance1": {
            "instance_type": "t2.micro"
          }, 
          "instance2": {
            "instance_type": "t2.micro"
          }  
        }, 
        "aws_subnet": {
          "subnet1" {
            "availability_zone": "usa-west-2a"
          }  
        }  
      } 
    } 

Provider
~~~~~~~~

A Terraform configuration contains one or more provider sections. Unlike
resources and data sources providers don't have a name and are distinguised 
by their ``alias`` attribute instead. Therefore multiple instances of the same
provider type are encoded as a list.

Example:

* Two ``aws`` providers with aliases ``aws1`` and ``aws2``.
* One ``google`` provider with alias ``google1``.

.. code-block:: json

   {
     "provider": { 
       "aws": [ 
         { 
           "region": "us-east-1",
           "alias": "aws1"
         },
         {
           "region": "us-east-2",
           "alias": "aws2"
         }
       ],
       "google": [
         {
           "region": "us-central-1",
           "alias": "google1"
         }
       ] 
     }
   }
 
Variable
~~~~~~~~

Variables are encoded as a dictionary whose keys are the names of the 
variables.

Example:

* Two variables names ``image_id`` and ``availability_zone_names``.

.. code-block:: json
 
   {
     "variable": {
       "image_id": {
         "type": "string"
       },
       "availability_zone_names": {
         "type": "list(string)",
         "default": [
           "us-west-1a",
           "us-west-1b"
         ]
       }
     }
   }

Variable references
~~~~~~~~~~~~~~~~~~~

When using a variable as a attribute value for a object, a reference are used.

Example:
* Variable ``image_id`` are used as name for instance.

.. code-block:: json

   {
     "variable": {
       "image_id": {
         "type": "string"
       }
     },
     "resource": {
       "aws_instance": {
         "instance1": {
           "instance_type": "${var.image_id}"
         }
       }
     }
   }

Output Values
~~~~~~~~~~~~~

Output values are encoded as a dictionary whose keys are the names of the 
value.

Example:

* Output values for two resources. 

.. code-block:: json
 
   {
     "output": {
       "instance1_ip_addr": {
         "value": "instance1.server.private_ip"
       },
       "instance2_ip_addr": {
         "value": "instance2.server.private_ip"
       },
     }
   }

Local Values
~~~~~~~~~~~~

Local values are encoded as a dictionary whose keys are the names of the 
value.

Example:

.. code-block:: json 
 
   {
     "locals": {
       "service_name": "forum",
       "owner": "Community Team",
       "Service": "local.service_name",
       "Owner": "local.owner"
     }
   }

   
Modules
~~~~~~~

Module calls are dictionaries keyed by the name of the module and 
module arguments as values.

.. note:: In contrast to calling existing modules, creating modules is 
          not supported by Python-Terrascript as Python functions 
          could be used as an alternative.   

Example: 

* Calling module ``vpc``.


.. code-block:: json

   {
     "module": {
       "vpc": {
         "source": "terraform-aws-modules/vpc/aws",
         "version": "2.9.0"
       }
     }
   }

Data Sources
~~~~~~~~~~~~

Data sources are coded as nested dictionaries. The top-level key is the type
of the resource. The second-level key is the name of the data source.

Example:

* Two ``aws_ami`` data sources named ``ami1`` and ``ami2``.

.. code-block:: json

   {
     "data": {
       "aws_ami": {
         "ami1": {
           "most_recent": true
         },
         "ami2": {
           "most_recent": true
         },
       }
     }
   }

Expressions
~~~~~~~~~~~


Functions
~~~~~~~~~

Functions are encoded as text. Example: ``"content": "file('hello_world.txt')"``.

Terraform Settings
~~~~~~~~~~~~~~~~~~

Terraform settings are a simple dictionary although the values of settings
may contain nested data structures.

Example:

* Terraform backend configuration.

.. code-block:: json 

   {
     "terraform": { 
       "backend": {
         "s3": {
           "bucket": "mybucket"
         }
       }
     }
   }
