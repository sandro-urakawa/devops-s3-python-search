import boto3
import os
import sys, getopt

endpoint_url = "http://localhost.localstack.cloud:4566"

def main(argv):
    s3_bucket_name = ''
    substring = ''
    ignore_case = False
    search_aws = False
    found = 0
    help_text = """usage: python search-s3.py -b|--s3_bucket_name <s3_bucket_name> -s|--substring <substring>
            Optional parameters:
                -i | --ignore-case
                -a | --aws"""

    try:
        opts, args = getopt.getopt(argv,"hiab:s:",["s3_bucket_name=","substring=","ignore-case","aws"])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (help_text)
            sys.exit()
        elif opt in ("-b", "--s3_bucket_name"):
            s3_bucket_name = arg
        elif opt in ("-s", "--substring"):
             substring = arg
        elif opt in ("-i", "--ignore-case"):
             ignore_case = True
        elif opt in ("-a", "--aws"):
             search_aws = True

    #verify required parameters
    if s3_bucket_name == '' or substring == '':
        print (help_text)
        sys.exit(2)
    
    if (search_aws):
        #client using AWS
        client = boto3.client("s3")
    else:
        #client using localstack
        client = boto3.client("s3", endpoint_url=endpoint_url)
    
    #list objects from s3 bucket / raise a error if bucket doesn't exist
    try:
        response = client.list_objects_v2(Bucket=s3_bucket_name)
    except client.exceptions.NoSuchBucket:
        print("Bucket", s3_bucket_name, "does not exist")
        sys.exit(2)
    
    files = response.get("Contents")
    for file in files:
        filename = "tmp/" + file['Key']
        #create subdir if necessary
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        #download and write file
        with open(filename, 'wb') as data:
            client.download_fileobj(s3_bucket_name,file['Key'],data)
        
        #read file
        with open(filename, 'r') as data:
            lines = data.readlines()
            for line in lines:
                if (ignore_case):
                    line_case = line.casefold()
                    substring_case = substring.casefold()
                    if line_case.find(substring_case) != -1:
                        print(substring, 'string exists in', file['Key'])
                        print('Line Number:', lines.index(line)+1)
                        print('Line:', line)
                        found = found + 1
                else:
                    if line.find(substring) != -1:
                        print(substring, 'string exists in', file['Key'])
                        print('Line Number:', lines.index(line)+1)
                        print('Line:', line)
                        found = found + 1
    if found == 0:
        print(substring, "not found in any file")
        exit()
        
if __name__ == "__main__":
    main(sys.argv[1:])
