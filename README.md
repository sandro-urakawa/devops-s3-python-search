# devops-s3-python-search
Python script to search for substrings in files in an S3 bucket - POC.

# Localstack
* https://github.com/localstack/localstack

## Requirements
* python (Python 3.7 up to 3.10 supported)
* pip (Python package manager)
* Docker

## Install
`pip install localstack`

## Start
`localstack start -d`

## Status
`localstack status services`

# S3 Sample Data
## Terraform
* https://www.terraform.io/

### Install (MacOS)
```
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

## tflocal
* https://docs.localstack.cloud/integrations/terraform/#using-the-tflocal-script

### Install
`pip install terraform-local`

### Populate Localstack S3 with sample files
```
cd terraform-local
tflocal init
tflocal apply
...
Enter a value: yes
...
```
### Check if the bucket and files are in place
* https://docs.localstack.cloud/integrations/aws-cli/#localstack-aws-cli-awslocal

`pip install awscli-local`

```
% awslocal s3 ls
2022-10-30 23:46:05 sample-bucket
```

```
% awslocal s3 ls sample-bucket
                           PRE dir1/
                           PRE dir2/
2022-10-30 23:46:07         18 file1.txt
2022-10-30 23:46:07         21 file2.txt
2022-10-30 23:46:07        576 file3.txt
```


# Using python search-s3.py script
## Python Virtualenv
* https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
```
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
```

## Create Virtualenv and install dependencies 
* In the repository root directory:
```
python3 -m venv python
cd python
source bin/activate
pip install -r requirements.txt
```

## Script usage:
`python search-s3.py -b|--s3_bucket_name <s3_bucket_name> -s|--substring <substring>`

* Example:

```
% python search-s3.py -b sample-bucket -s random
random string exists in dir1/file2.txt
Line Number: 2
Line: random

random string exists in dir2/file2.txt
Line Number: 2
Line: random

random string exists in file2.txt
Line Number: 2
Line: random
```

# Additional features
## Case insensitive search
* Add `-i` parameter to script, example:
```
% python search-s3.py -b sample-bucket -s random -i        
random string exists in dir1/file1.txt
Line Number: 2
Line: Random

random string exists in dir1/file2.txt
Line Number: 2
Line: random

random string exists in dir2/file1.txt
Line Number: 2
Line: Random

random string exists in dir2/file2.txt
Line Number: 2
Line: random

random string exists in file1.txt
Line Number: 2
Line: Random

random string exists in file2.txt
Line Number: 2
Line: random
```

## Using in AWS 
### IAM User (Access Key and Secret)
* Create an IAM user with `Programmatic access` to generate an Access Key and Secret
* The policy for the user needs these permissions, change `sample-bucket-bru2pznp` with your bucket name:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:PutBucketTagging",
                "s3:PutBucketAcl",
                "s3:CreateBucket",
                "s3:DeleteObject",
                "s3:GetBucketAcl",
                "s3:DeleteBucketPolicy",
                "s3:DeleteBucket"
            ],
            "Resource": [
                "arn:aws:s3:::sample-bucket-bru2pznp/*",
                "arn:aws:s3:::sample-bucket-bru2pznp"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Resource": [
                "arn:aws:s3:::sample-bucket-bru2pznp/*",
                "arn:aws:s3:::sample-bucket-bru2pznp"
            ]
        }
    ]
}
```

### Install AWS CLI
* https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

### Config AWS CLI
```
% aws configure  
AWS Access Key ID [None]: XXXXXXXXXXXX
AWS Secret Access Key [None]: XXXXXXXXXXXXXXXX
Default region name [None]: eu-west-1
Default output format [None]: json
```

### Populate AWS S3 with sample files
**Note: change the bucket name in the variables.tf file, if an error occurs informing that this name is already in use.**
```
cd terraform-aws
terraform init
terraform apply
...
Enter a value: yes
...
```

### Use the script with -a or --aws parameter
* Example:

```
% python search-s3.py -b sample-bucket-bru2pznp -s random -a
random string exists in dir1/file2.txt
Line Number: 2
Line: random

random string exists in dir2/file2.txt
Line Number: 2
Line: random

random string exists in file2.txt
Line Number: 2
Line: random
```
