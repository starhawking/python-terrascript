# Provisioners

Provisioners can be attached to resources and connections are attached to provisioners.

```python
from terrascript import provider, provisioner, connection, dump
from terrascript.aws.r import aws_instance

provider('aws', access_key='ACCESS_KEY_HERE', 
         secret_key='SECRET_KEY_HERE', region='us-east-1')

conn = connection(type='ssh', user='root', password='password')

prov = provisioner('file', source='conf/myapp.conf', destination='/etc/myapp.conf',
                   connection=conn)
     
example = aws_instance('example', ami='ami-2757f631', instance_type='t2.micro',
                       provisioner=prov)
                       
print(dump())
```

The Terraform JSON configuration.


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
        "instance_type": "t2.micro",
        "provisioner": {
          "file": {
            "connection": {
              "password": "password",
              "type": "ssh",
              "user": "root"
            },
            "destination": "/etc/myapp.conf",
            "source": "conf/myapp.conf"
          }
        }
      }
    }
  }
}
```