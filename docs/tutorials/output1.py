import terrascript
import terrascript.provider
import terrascript.resource

config = terrascript.Terrascript()

# AWS provider
config += terrascript.provider.aws(region="us-east-1")

# Define Variable and add to config
v = terrascript.Variable("image_id", type="string")
config += v

# Define AWS EC2 instance and add to config
i = terrascript.resource.aws_instance("example", instance_type="t2.micro", ami=v)
config += i

# Output the instance's private IP
config += terrascript.Output(
    "instance_ip_addr",
    value=i.private_ip,
    description="The private IP address of the instance.",
)
