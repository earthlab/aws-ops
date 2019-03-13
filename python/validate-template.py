import boto3
import glob

client = boto3.client('cloudformation')

file = glob.glob('2*-ec2-template.json')

assert len(file) == 1

with open(file[0], 'r') as f:
    response = client.validate_template(TemplateBody=f.read())

print(response)
