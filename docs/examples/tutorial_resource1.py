import terrascript
import terrascript.provider
import terrascript.resource

config = terrascript.Terrascript()

# AWS provider
config += terrascript.provider.aws(region="us-east-1")

# Add an AWS S3 bucket resource
config += terrascript.resource.aws_s3_bucket(
    "mybucket",
    bucket="mybucket",
    acl="private",
    tags={"Name": "My bucket", "Environment": "Dev"},
)
