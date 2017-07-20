# python-terrascript

**Terrascript** provides a method of generating [Terraform](https://www.terraform.io) 
files, while harnessing all the features the Python language provides.

*This project is currently in the planning stage and the code will probably not yet work!*

```python
from terrascript.aws.r import aws_instance

PROD=True
if PROD:
  instance_count = 2
else:
  instance_count = 1

for i in range(0, instance_count):
    aws_instance('instance'+str(i), ami='ami-22b9a343', instance_type='t2.micro')
```

Running the Python 3 script above will emit the following.

```hcl
resource "aws_instance" "instance0" {
  ami = "ami-22b9a343"
  instance_type = "t2.micro"
}

resource "aws_instance" "instance1" {
  ami = "ami-22b9a343"
  instance_type = "t2.micro"
}
```

**IMPORTANT: Terrascript does not perform any error checking whatsoever. It is entierly 
up to you to ensure that the generated output makes sense to Terraform.**

More details can be found on the following pages.

* [Interpolation](docs/interpolation.md)

*The rest of this README is TODO!!!*
