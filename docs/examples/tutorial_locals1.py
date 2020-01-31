import terrascript
import terrascript.provider
import terrascript.resource

config = terrascript.Terrascript()

# AWS provider
config += terrascript.provider.aws(region="us-east-1")

# Local values as Python variables
tags = {"service_name": "forum", "owner": "Community Team"}

# Resource with two provisioners
config += terrascript.resource.aws_instance(
    "instance1", instance_type="t2.micro", ami="ami-4bf3d731", tags=tags
)
