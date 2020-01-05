provider "aws" {
  alias   = "east"
  region  = "us-east-1"
}

provider "aws" {
  alias   = "west"
  region  = "us-west-1"
}