# Variables

The Python code below shows how to define Terraform input and output variables.

```python
from terrascript import provider, dump, variable
from terrascript.aws.r import aws_instance

var_access_key = variable('access_key')
var_secret_key = variable('secret_key')
var_region = variable('region', default='us-east-1')


provider('aws', access_key=var_access_key, 
         secret_key=var_secret_key,
         region=var_region)
         
example = aws_instance('example', ami='ami-2757f631', instance_type='t2.micro')

output('example_public_ip', value=example.public_ip, description='Public IP of example')

print(dump())
```

The variables are interpolated into the ``provider`` and ``output`` sections..

```json
{
  "output": {
    "example_public_ip": {
      "description": "Public IP of example",
      "value": "${aws_instance.example.public_ip}"
    }
  },
  "provider": {
    "aws": {
      "access_key": "${var.access_key}",
      "region": "${var.region}",
      "secret_key": "${var.secret_key}"
    }
  },
  "resource": {
    "aws_instance": {
      "example": {
        "ami": "ami-2757f631",
        "instance_type": "t2.micro"
      }
    }
  },
  "variable": {
    "access_key": {},
    "region": {
      "default": "us-east-1"
    },
    "secret_key": {}
  }
}

```