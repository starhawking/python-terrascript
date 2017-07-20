# Interpolation

**Terrascript** supports Terraform interpolation.

## User string variables

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

##  User map variables

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

## User list variables

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

## Attributes of other resources

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

