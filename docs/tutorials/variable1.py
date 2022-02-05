import terrascript
import terrascript.provider.aws
import terrascript.resource.aws

config = terrascript.Terrascript()

# AWS provider
config += terrascript.provider.aws.aws(region="us-east-1")

# Define Variable and add to config
v = terrascript.Variable("image_id", type="string")
config += v

# AWS EC2 instance referencing the variable.
config += terrascript.resource.aws.aws_instance(
    "example",
    instance_type="t2.micro",
    ami=v,
)
