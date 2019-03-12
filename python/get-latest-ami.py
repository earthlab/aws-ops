# from https://github.com/bwood/latest-ami
import boto3
import sys

from dateutil import parser


def newest_image(list_of_images):
    latest = None

    for image in list_of_images:
        if not latest:
            latest = image
            continue

        if parser.parse(image["CreationDate"]) > parser.parse(latest["CreationDate"]):
            latest = image

    return latest


client = boto3.client("ec2", region_name="us-west-2")

filters = [
    {"Name": "name", "Values": ["*-earthlab-docker"]},
    {"Name": "owner-id", "Values": ["732215511434"]},
    {"Name": "state", "Values": ["available"]},
]

response = client.describe_images(Filters=filters)
source_image = newest_image(response["Images"])
print(source_image["ImageId"])
