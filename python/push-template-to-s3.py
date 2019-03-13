import boto3
import glob

s3 = boto3.resource('s3')

file = glob.glob('2*-ec2-template.json')
assert len(file) == 1

s3.meta.client.upload_file(file[0], 'earthlab-cloudformation', file[0])
