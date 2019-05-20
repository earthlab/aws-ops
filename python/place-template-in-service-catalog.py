""" Update the EC2 product in the service catalog. """

import boto3
import glob
from datetime import datetime

client = boto3.client("servicecatalog")

s3 = boto3.client("s3")

file = glob.glob("2*-ec2-template.json")
assert len(file) == 1

template_url = "{}/{}/{}".format(
    s3.meta.endpoint_url, "earthlab-cloudformation", file[0]
)

response = client.create_provisioning_artifact(
    ProductId="prod-jorfwrdc4ayte",
    Parameters={
        "Info": {"LoadTemplateFromURL": template_url},
        "Type": "CLOUD_FORMATION_TEMPLATE",
        "Name": "v" + datetime.today().strftime('%Y-%m-%d_%H:%M:%S'),
    },
)
