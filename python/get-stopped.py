import boto3
import re
from datetime import datetime, timedelta

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
rsp = client.describe_instances()
if rsp:
    instances_to_terminate = []
    for reservation in rsp.get("Reservations"):
        status = reservation["Instances"][0]
        if status['State']['Name'] == 'stopped':
            stopped_reason = status['StateTransitionReason']
            current_time = rsp['ResponseMetadata']['HTTPHeaders']['date']
            stopped_time = re.findall('.*\((.*)\)', stopped_reason)[0]
            current_dt = datetime.strptime(current_time,
                                           '%a, %d %b %Y %H:%M:%S %Z')
            stopped_dt = datetime.strptime(stopped_time,
                                           '%Y-%m-%d %H:%M:%S %Z')
            time_stopped = datetime.now() - stopped_dt
            if time_stopped > timedelta(days=7):
                instances_to_terminate.append(status["InstanceId"])

if instances_to_terminate:
    print("There are instances to terminate:")
    print(instances_to_terminate)
    ec2.instances.filter(InstanceIds=instances_to_terminate).stop()
    ec2.instances.filter(InstanceIds=instances_to_terminate).terminate()
