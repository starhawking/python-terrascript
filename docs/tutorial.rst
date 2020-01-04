Tutorial
---------

This section explains the different Terrascript Python classes that can
be used to generate a Terraform configuration.

Since release 0.8.0 all Terrascript classes are available by importing
just four modules.

.. code-block:: python
   :linenos:

    import terrascript
    import terrascript.provider
    import terrascript.resource
    import terrascript.data

.. note:: The old layout, e.g. ```import terarscript.aws.r``` is still available
          for backward compatibility but it's use is discouraged. 

Provider
~~~~~~~~

Providers_ can be found in the ```terrascript.provider``` module, with one class
for each provider. Terrascript supports most Terraform providers. The full list 
can be found in the :doc:`appendices.

.. code-block:: python
   :linenos:

    import terrascript
    import terrascript.provider

    config = terrascript.Terrascript()

    # Amazon Web Service with aliases
    config += terrascript.provider.aws(alias="east", region="us-east-1")
    config += terrascript.provider.aws(alias="west", region="us-west-1")

.. _Providers: https://www.terraform.io/docs/providers/index.html

Resource
~~~~~~~~

Resources can be found in the ```terrascript.resource``` module. The example below shows
the original HCL syntax for creating an AWS S3 bucket and the equivalent Python code. 

.. code-block:: none
   :linenos:

    provider "aws" {
      region     = "us-east-1"
    }

    resource "aws_s3_bucket" "mybucket" {
        bucket = "mybucket"
        acl    = "private"
        tags = {
            Name        = "My bucket"
            Environment = "Dev"
        }
    }

And here is the same as a Python script. The first argument to ``terrascript.resource.aws_s3_bucket()```
is the Terraform label under which it can be referenced later. Note how the ```tags``` is a dictionary
as in the HCL syntax.

.. code-block:: python
   :linenos:

    import terrascript
    import terrascript.provider
    import terrascript.resource

    config = terrascript.Terrascript()

    # AWS provider
    config += terrascript.provider.aws(region="us-east-1")

    # Add an AWS S3 bucket resource
    config += terrascript.resource.aws_s3_bucket("mybucket", bucket="mybucket",
                                                 acl="private",
                                                 tags={
                                                     "Name": "My bucket",
                                                     "Environment": "Dev"
                                                 })

Data Source
~~~~~~~~~~~

Data Sources are located in the ```terrascript.data``` module. The example creates a Google 
Compute Instance based on the Debian-9 image. First the Terrascript HCL syntax.

.. code-block:: none
   :linenos:

    provider "google" {
        credentials = "${file("account.json")}"
        project     = "myproject"
        region      = "us-central1"
    }

    data "google_compute_image" "debian9" {
        family  = "debian-9"
        project = "debian-cloud"
    }

    resource "google_compute_instance" "myinstance" {
        name         = "test"
        machine_type = "n1-standard-1"
        zone         = "us-central1-a"
        boot_disk {
            initialize_params {
                image = data.google_compute_image.debian9.self_link
            }
        }
        network_interface {
            network = "default"
            access_config {
                // Ephemeral IP
            }
        }
    }

.. code-block:: python
   :linenos:

    import terrascript
    import terrascript.provider
    import terrascript.resource

    config = terrascript.Terrascript()

    # Google Cloud Compute provider
    config += terrascript.provider.google(credentials='${file("account.json")}',
                                          project='myproject', region='us-central1')

    # Google Compute Image (Debian 9) data source
    config += terrascript.data.google_compute_image("image", family="debian-9")

    # Add Google Compute Instance resource
    config += terrascript.resource.google_compute_instance("myinstance",
                                                           name="myinstance",
                                                           machine_type="n1-standard-1",
                                                           zone="us-central1-a",
                                                           boot_disk={
                                                                "initialize_params": {
                                                                    "image": "data.google_compute_image.image.self_link"
                                                                }    
                                                           },
                                                           network_interface={
                                                               "network": "default",
                                                               "access_config": {}
                                                           })

The example above is mostly a one-to-one adaptation of the HCL syntax. Let's make some changes
to show how generating Terraform configurations through Python-Terrascript may help.
* Define the Google Compute Image family and Google Compute Instance machine type at the beginning 
  of the script so they are easier to change (lines X,X,X and X).
* Reference an instance of the Python-Terrascript class ```terrascript.data.google_compute_image()```
  as the boot disk image (line X)
                                          

.. code-block:: python
   :linenos:

    IMAGE_FAMILY = "debian-9"
    MACHINE_TYPE = "n1-standard-1"

    import terrascript
    import terrascript.provider
    import terrascript.resource

    config = terrascript.Terrascript()

        # Google Cloud Compute provider
    config += terrascript.provider.google(credentials='${file("account.json")}",
                                          project="myproject", region="us-central1")

    # Google Compute Image (Debian 9) data source
    image = terrascript.data.google_compute_image("image", family=IMAGE_FAMILY)
    config += image

    # Add Google Compute Instance resource
    config += terrascript.resource.google_compute_instance("myinstance",
                                                           name="myinstance",
                                                           machine_type=MACHINE_TYPE,
                                                           zone="us-central1-a",
                                                           boot_disk={
                                                                "initialize_params": {
                                                                    "image": image.self_link
                                                                }    
                                                           },
                                                           network_interface={
                                                               "network": "default",
                                                               "access_config": {}
                                                           })

Variable
~~~~~~~~

Output
~~~~~~

Module
~~~~~~

Terraform
~~~~~~~~~

Locals
~~~~~~