# Example: AWS Elastic IP

This example is based on the [Elastic IP example](https://github.com/terraform-providers/terraform-provider-aws/tree/master/examples/eip)
distributed with the Terraform source code.

```python
from terrascript import variable, provider, dump
from terrascript.fn import lookup, file
from terrascript.aws.r import aws_eip, aws_security_group, aws_instance

# From variables.tf
aws_region = variable('aws_region', default='us-east-1', description='The AWS region to create things in.')
aws_amis = variable('aws_amis', default={'us-east-1': 'ami-5f709f34', 'us-west-2': 'ami-7f675e4f'})
key_name = variable('key_name', description='Name of the SSH keypair to use in AWS.')

# From main.tf
provider('aws', region=aws_region)

sg = aws_security_group('default', name='eip_example', description='Used in the terraform',
                        ingress=[{'from_port': 22, 'to_port': 22, 
                                  'protocol': 'tcp', 'cidr_blocks': ['0.0.0.0/0']},
                                 {'from_port': 80, 'to_port': 80, 
                                  'protocol': 'tcp', 'cidr_blocks': ['0.0.0.0/0']}
                        ],
                        egress=[{'from_port': 0, 'to_port': 0, 
                                  'protocol': '-1', 'cidr_blocks': ['0.0.0.0/0']}
                        ])
                        
web = aws_instance('web', instance_type='t2.micro', ami=lookup(aws_amis, aws_region),
                   key_name=key_name, security_groups=[sg], user_data=file('userdata.sh'),
                   tags={'Name': 'eip-example'})
                   
eip = aws_eip('default', instance=web.id, vpc=True)

# From output.tf
output('address', value=web.private_ip)
output('elatsic ip', value=eip.public_ip)

print(dump())
```

BUG: There is currently a bug that does not interpolate "${file(userdata.sh)}" correctly!!!


```json
{
  "output": {
    "address": {
      "value": "${aws_instance.web.private_ip}"
    },
    "elatsic ip": {
      "value": "${aws_eip.default.public_ip}"
    }
  },
  "provider": {
    "aws": {
      "region": "${var.aws_region}"
    }
  },
  "resource": {
    "aws_eip": {
      "default": {
        "instance": "${aws_instance.web.id}",
        "vpc": true
      }
    },
    "aws_instance": {
      "web": {
        "ami": "${lookup(var.aws_amis,var.aws_region)}",
        "instance_type": "t2.micro",
        "key_name": "${var.key_name}",
        "security_groups": [
          "aws_security_group.default"
        ],
        "tags": {
          "Name": "eip-example"
        },
        "user_data": "${file(userdata.sh)}"
      }
    },
    "aws_security_group": {
      "default": {
        "description": "Used in the terraform",
        "egress": [
          {
            "cidr_blocks": [
              "0.0.0.0/0"
            ],
            "from_port": 0,
            "protocol": "-1",
            "to_port": 0
          }
        ],
        "ingress": [
          {
            "cidr_blocks": [
              "0.0.0.0/0"
            ],
            "from_port": 22,
            "protocol": "tcp",
            "to_port": 22
          },
          {
            "cidr_blocks": [
              "0.0.0.0/0"
            ],
            "from_port": 80,
            "protocol": "tcp",
            "to_port": 80
          }
        ],
        "name": "eip_example"
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
    },
    "key_name": {
      "description": "Name of the SSH keypair to use in AWS."
    }
  }
}
```
