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

