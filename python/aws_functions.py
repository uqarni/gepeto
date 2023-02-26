import os
import boto3

aws_access_key_id = 'AKIAZDUCM7JQVMLYYOOX'
aws_secret_access_key = os.environ['AKIAZDUCM7JQVMLYYOOX']

# Set the name of your S3 bucket and the filename
bucket_name = 'gepeto'
file_name = 'file_path'

# Connect to S3 using the AWS access keys
s3 = boto3.client('s3', 
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# Upload the file to S3
s3.upload_file(file_name, bucket_name, file_name.split('/')[-1])