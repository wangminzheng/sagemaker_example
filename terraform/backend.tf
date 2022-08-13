# set terraform backend to use s3 bucket to manage state
terraform {
  backend "s3" {
    bucket = "stan-terraform-state-management"
    key    = "stan-test-state-1.tfstate"
    region = "us-east-1"
  }
}
provider "aws" {
  region = "us-east-1"
}