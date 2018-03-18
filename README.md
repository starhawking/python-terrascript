# python-terrascript

[![PyPI](https://img.shields.io/pypi/v/terrascript.svg?style=flat-square)](https://pypi.python.org/pypi/terrascript)
[![license](https://img.shields.io/github/license/mjuenema/python-terrascript.svg?style=flat-square)](https://opensource.org/licenses/BSD-2-Clause)
[![GitHub issues](https://img.shields.io/github/issues/mjuenema/python-terrascript.svg?style=flat-square)](https://github.com/mjuenema/python-terrascript/issues)
[![Travis](https://img.shields.io/travis/mjuenema/python-terrascript.svg?style=flat-square)](https://www.travis-ci.org/mjuenema/python-terrascript)
[![Codecov](https://img.shields.io/codecov/c/github/mjuenema/python-terrascript.svg?style=flat-square)](https://codecov.io/gh/mjuenema/python-terrascript)

**Terrascript** provides a method of generating [Terraform](https://www.terraform.io)
files, while harnessing all the features the Python 3 language provides.

IMPORTANT: Release 0.5.0 introduced changes that are not backwards compatible with
earlier releases. The examples in this document describe the current
release of **Terrascript** while the [old README](README_OLD.md) covers releases
up to 0.4.1.

## Example

As an example let's translate the following Terraform configuration into **Terrascript**.

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
from terrascript import Terrascript, provider
from terrascript.aws.r import aws_instance

ts = Terrascript()

# Add a provider.
ts += provider('aws', access_key='ACCESS_KEY_HERE',
               secret_key='SECRET_KEY_HERE', region='us-east-1')

# Add an AWS EC2 instance.
ts += aws_instance('example', ami='ami-2757f631', instance_type='t2.micro')

# Print the JSON-style configuration to stdout.
print(ts.dump())
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

**IMPORTANT: Terrascript does not perform any error checking whatsoever. It is entirely 
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

IMPORTANT: These examples only works with **Terrascript** releases up to 0.4.1.

This section lists some more advanced examples.

* [AWS Elastic IP (eip)](doc/examples/aws_eip.md)
* [Example based on chapter 4 of "Terraform: Up and Running"](doc/examples/module_webserver_cluster).

## Status

**Terrascript** works with Terraform release 0.10.0 and later. Earlier versions
of Terraform should also work fine with the exception of the `Terrascript.validate()`
method.

All Terraform providers (as of 21-Nov-2017) are supported but most haven't seen
any testing at all. Please let me know if you run into any problems.

I'd also like to add more examples.

## FAQ

* [Why no error checking?](doc/faq/no_error_checking.md)
