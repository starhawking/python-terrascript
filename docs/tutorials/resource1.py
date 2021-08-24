import terrascript
import terrascript.provider.hashicorp.aws
import terrascript.resource.hashicorp.aws

config = terrascript.Terrascript()

# AWS provider
config += terrascript.provider.hashicorp.aws.aws(region="us-east-1")

# Add an AWS S3 bucket resource
config += terrascript.resource.hashicorp.aws.aws_s3_bucket(
    "mybucket",
    bucket="mybucket",
    acl="private",
    tags={"Name": "My bucket", "Environment": "Dev"},
)
