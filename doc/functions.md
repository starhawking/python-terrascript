# Functions

Terraform functions are supported through `terrascript.function.*` or its shortcuts
`terrascript.func.*`, `terrascript.fn.*`, `terrascript.f.*`. 

```python
from terrascript import function, variable, dump
from terrascript.aws.r import aws_instance

aws_region = variable('aws_region', default='us-east-1', description='The AWS region to create things in.')
aws_amis = variable('aws_amis', default={'us-east-1': 'ami-5f709f34', 'us-west-2': 'ami-7f675e4f'})

aws_instance('web', instance_type='t2.micro', ami=function.lookup(aws_amis, aws_region))

print(dump())
```

The Terraform configuration 

```json
{
  "resource": {
    "aws_instance": {
      "web": {
        "ami": "${lookup(var.aws_amis,var.aws_region)}",
        "instance_type": "t2.micro"
      }
    }
  },
  "variable": {
    "aws_amis": {
      "default": {
        "us-east-1": "ami-5f709f34",
        "us-west-2": "ami-7f675e4f"
      }
    },
    "aws_region": {
      "default": "us-east-1",
      "description": "The AWS region to create things in."
    }
  }
}
```