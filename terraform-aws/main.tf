terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region  = var.region
  profile = "default"
}

# Create a S3 Bucket
resource "aws_s3_bucket" "bucket" {
  bucket    = var.bucket_name

  tags = {
    Name        = var.bucket_name
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_acl" "bucket_acl" {
  bucket = aws_s3_bucket.bucket.id
  acl    = "private"
}

#Upload sample files
resource "aws_s3_bucket_object" "object" {
  for_each = fileset("../s3/", "*")

  bucket = aws_s3_bucket.bucket.id
  key    = each.value
  source = "../s3/${each.value}"
  etag   = filemd5("../s3/${each.value}")
}

resource "aws_s3_bucket_object" "object_dir1" {
  for_each = fileset("../s3/", "*")

  bucket = aws_s3_bucket.bucket.id
  key    = "dir1/${each.value}"
  source = "../s3/${each.value}"
  etag   = filemd5("../s3/${each.value}")
}

resource "aws_s3_bucket_object" "object_dir2" {
  for_each = fileset("../s3/", "*")

  bucket = aws_s3_bucket.bucket.id
  key    = "dir2/${each.value}"
  source = "../s3/${each.value}"
  etag   = filemd5("../s3/${each.value}")
}