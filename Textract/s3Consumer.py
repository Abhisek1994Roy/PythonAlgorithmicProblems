import boto3
import sys

BUCKET_NAME = 'ksf-raw-data-dev'

file_name = sys.argv[1]

s3 = boto3.resource(
    's3',
    aws_access_key_id='AKIA6EPTKPHR2RILQDFM',
    aws_secret_access_key='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'
)

def downloadFile(fileName):
    #Download object to the file
    s3.Bucket(BUCKET_NAME).download_file(fileName,file_name)

downloadFile(file_name)




