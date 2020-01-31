import terrascript
import terrascript.provider
import terrascript.resource

config = terrascript.Terrascript()

# AWS provider
config += terrascript.provider.aws(region="us-east-1")

# Define Variable and add to config
v = terrascript.Variable("image_id", type="string")
config += v

# AWS EC2 instance referencing the variable.
config += terrascript.resource.aws_instance("example", instance_type="t2.micro", ami=v)
