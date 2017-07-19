# python-terrascript

**Terrascript** provides a method of generating [Terraform](https://www.terraform.io) 
files, while harnessing all the features the Python language provides.

*This project is currently in the planning stage and the code will probably not yet work!*

## Simple Example

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

## Interpolation

**Terrascript** supports Terraform interpolation.

### User string variables

```python
from terrascript import var
from terrascript.aws.r import aws_instance

ami = var('ami')
aws_instance('instance', ami=ami, instance_type='t2.micro')
```

```hcl
resource "aws_instance" "instance" {
  ami = "${var.ami}"
  instance_type = "t2.micro"
}
```

###  User map variables

```python
from terrascript import map
from terrascript.aws.r import aws_instance

amis = map('amis')
aws_instance('instance', ami=amis['us-east-1'], instance_type='t2.micro')
```

```hcl
resource "aws_instance" "instance" {
  ami = "${var.amis["us-east-1"]}"
  instance_type = "t2.micro"
}
```

### User list variables

```python
from terrascript import list
from terrascript.aws.r import aws_instance

amis = list(['ami-12345678', 'ami-98765432'])

aws_instance('instance', ami=amis[1], instance_type='t2.micro')
```

```hcl
resource "aws_instance" "instance" {
  ami = "${var.amis[1]}"
  instance_type = "t2.micro"
}
```

### Attributes of other resources

```python
first = aws_instance('first', ami='ami-12345678', instance_type='t2.micro')

# Force second instance into same AZ.
aws_instance('second', ami='ami-12345678', instance_type='t2.micro',
             availability_zone=first.availability_zone)
```

```hcl
resource "aws_instance" "first" {
  ami = "ami-22b9a343"
  instance_type = "t2.micro"
}

resource "aws_instance" "second" {
  ami = "ami-22b9a343"
  instance_type = "t2.micro"
  availability_zone = "${aws_instance.first.availability_zone}"
}
```

*The rest of this README is TODO!!!*
