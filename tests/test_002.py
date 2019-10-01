# https://www.terraform.io/docs/providers/aws/guides/custom-service-endpoints.html

import terrascript
import terrascript.provider
import terrascript.resource

from shared import assert_equals_json


def test():
    """Provider Endpoints (002)

       Configure the AWS Provider

            provider "aws" {
                version = "~> 2.0"
                region  = "us-east-1"
                    endpoints {
                        dynamodb = "http://localhost:4569"
                        s3       = "http://localhost:4572"
                    }
            }

       Create a VPC

            resource "aws_vpc" "example" {
                cidr_block = "10.0.0.0/16"
            }

    """

    config = terrascript.Terrascript()

    config += terrascript.provider.aws(version='~> 2.0',
                                       region='us-east-1',
                                       endpoints=dict(dynamodb='http://localhost:4569',
                                                      s3='http://localhost:4572')
                                       )

    config += terrascript.resource.aws_vpc('example', cidr_block='10.0.0.0/16')

    assert_equals_json(config, 'test_002.tf.json')
