""" Fill in the latest AMI in the cloudformation template. """

import datetime


with open("latest_ami.txt", "r") as f:
    latest_ami = f.read().replace("\n", "")

todays_date = datetime.datetime.today().strftime("%Y-%m-%d")

with open("cloudformation/basic-ec2-template.json", "rt") as fin:
    with open("{}-ec2-template.json".format(todays_date), "wt") as fout:
        for line in fin:
            fout.write(line.replace("{{AMIID}}", latest_ami))
