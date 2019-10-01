# Terraform: Up & Running by Yevgenij Brikman
# https://github.com/brikis98/terraform-up-and-running-code/tree/master/code/terraform/01-why-terraform/web-server

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

resource "aws_instance" "app" {
  instance_type     = "t2.micro"
  availability_zone = "us-east-2a"
  ami               = "ami-0c55b159cbfafe1f0"

  user_data = <<-EOF
              #!/bin/bash
              sudo service apache2 start
              EOF
}
"""


def test():
    """Terraform: Up & Running - Why Terraform - Web Server"""
    import terrascript
    import terrascript.provider
    import terrascript.resource

    USER_DATA = "#!/bin/bash\nsudo service apache2 start"

    config = terrascript.Terrascript()

    config += terrascript.provider.aws(region='us-east-2',
                                       version='~>2.0')

    config += terrascript.resource.aws_instance('app',
                                                instance_type='t2.micro',
                                                availability_zone='us-east-2a',
                                                ami='ami-0c55b159cbfafe1f0',
                                                user_data=USER_DATA)

    shared.assert_deep_equal(config, 'test_TUAR_why_terraform.tf.json')
