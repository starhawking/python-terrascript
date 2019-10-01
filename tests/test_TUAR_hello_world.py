# Terraform: Up & Running 2nd Edition by Yevgenij Brikman
# https://github.com/brikis98/terraform-up-and-running-code/blob/2nd-edition/code/terraform/00-preface/hello-world/

import shared

HCL = """
terraform {
  required_version = ">= 0.12, < 0.13"
}

provider "aws" {
  region = "us-east-2"

  # Allow any 2.x version of the AWS provider
  version = "~> 2.0"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
"""


def test():
    """Terraform: Up & Running - Hello World"""
    import terrascript
    import terrascript.provider
    import terrascript.resource

    config = terrascript.Terrascript()
    config += terrascript.provider.aws(region='us-east-2', version='~>2.0')
    config += terrascript.resource.aws_instance(
        'example', ami='ami-0c55b159cbfafe1f0', instance_type='t2.micro')

    shared.assert_deep_equal(config, 'test_TUAR_hello_world.tf.json')
