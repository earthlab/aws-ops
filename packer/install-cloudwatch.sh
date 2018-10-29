#!/bin/bash

mkdir /tmp/AmazonCloudWatchAgent/
cd /tmp/AmazonCloudWatchAgent/
wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
rpm -U ./amazon-cloudwatch-agent.rpm
