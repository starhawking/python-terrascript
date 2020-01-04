provider "aws" {
    region     = "us-east-1"
}

resource "aws_s3_bucket" "mybucket" {
    bucket = "mybucket"
    acl    = "private"
    tags = {
        Name        = "My bucket"
        Environment = "Dev"
    }
}