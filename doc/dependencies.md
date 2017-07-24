# Dependencies

Dependencies are declared through the `depends_on` argument. The value must be a 
list.

```python
from terrascript import provider, dump
from terrascript.aws.r import aws_instance, aws_eip

provider('aws', access_key='ACCESS_KEY_HERE', 
         secret_key='SECRET_KEY_HERE', region='us-east-1')
         
example = aws_instance('example', ami='ami-2757f631', instance_type='t2.micro')
aws_eip('ip', instance=instance.id, depends_on=[example])
```

The JSON output shows how the "example" AWS Instance was referenced in the 
`depends_on` and `instance` arguments to the AWS Elastic IP resource.

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
    "aws_eip": {
      "ip": {
        "depends_on": [
          "aws_instance.example"
        ],
        "instance": "${aws_instance.example.id}"
      }
    },
    "aws_instance": {
      "example": {
        "ami": "ami-2757f631",
        "instance_type": "t2.micro"
      }
    }
  }
}
```