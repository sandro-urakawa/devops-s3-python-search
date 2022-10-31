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

`python search-s3.py -b sample-bucket -s random`

