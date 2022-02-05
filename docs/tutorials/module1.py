"""Terrascript module example based on https://registry.terraform.io/modules/terraform-aws-modules/ec2-instance/aws/"""

import terrascript
import terrascript.provider.aws

config = terrascript.Terrascript()

# AWS provider
config += terrascript.provider.aws.aws(region="us-east-1")

# AWS EC2 module
config += terrascript.Module(
    "ec2_cluster",
    source="terraform-aws-modules/ec2-instance/aws",
    version="~> 2.0",
    name="my-cluster",
    instance_count=5,
    ami="ami-ebd02392",
    instance_type="t2.micro",
    key_name="user1",
    monitoring=True,
    vpc_security_group_ids=["sg-12345678"],
    subnet_id="subnet-eddcdzz4",
)
