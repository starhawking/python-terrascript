# python-terrascript

**Terrascript** provides a method of generating [Terraform](https://www.terraform.io) 
files, while harnessing all the features the Python language provides.

## Example

As an example let's translate the following Terraform configuration into **terrascript**.

```hcl
provider "aws" {
  access_key = "ACCESS_KEY_HERE"
  secret_key = "SECRET_KEY_HERE"
  region     = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
```

The equivalent **terrascript** example would look like this.

```python
from terrascript import provider, dump
from terrascript.aws.r import aws_instance

provider('aws', access_key='ACCESS_KEY_HERE', 
         secret_key='SECRET_KEY_HERE', region='us-east-1')
         
aws_instance('example', ami='ami-2757f631', instance_type='t2.micro')

# Print the JSON-style configuration to stdout.
dump()
```

Creating instances of `provider` and `aws_instance` will automatically add them to
the Terraform configuration. Calling `dump()` will return the configuration in
JSON format.

```json
{
  "provider": {
    "aws": {
      "access_key": "ACCESS_KEY_HERE",
      "region": "us-east-1",
      "secret_key": "SECRET_KEY_HERE"
    }
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
```

**IMPORTANT: Terrascript does not perform any error checking whatsoever. It is entierly 
up to you to ensure that the generated output makes sense to Terraform.**

## Documentation

* [Dependencies](doc/dependencies.md)
* [Provisioners](doc/provisioners.md)
* [Variables](doc/variables.md)
* [Modules](doc/modules.md)
* [Backends](doc/backends.md)
* [Interpolation](doc/interpolation.md)
* [Functions](doc/functions.md)

## Examples

This section lists some more advanced examples.

* [AWS Elastic IP (eip)](doc/examples/aws_eip.md)

## FAQ

* [Why no error checking?](doc/faq/no_error_checking.md)
