# Deploy idle CPU alarms to stop EC2 instances
import boto3

account_id = boto3.client("sts").get_caller_identity().get("Account")
region = boto3.session.Session().region_name
client = boto3.client("cloudwatch")
ec = boto3.client("ec2")
reservations = ec.describe_instances()

exceptions = ["prf-"]

for r in reservations["Reservations"]:
    for i in r["Instances"]:
        instance_id = i["InstanceId"]
        for t in i["Tags"]:
            if t["Key"] == "Name":
                iname = t["Value"]
                name_excepted = any([e in iname for e in exceptions])
                if name_excepted:
                    continue
                else:
                    alarm_name = "CPU Alarm " + iname + instance_id
                    alarm = client.put_metric_alarm(
                        AlarmName=alarm_name,
                        MetricName="CPUUtilization",
                        Namespace="AWS/EC2",
                        Statistic="Maximum",
                        ComparisonOperator="LessThanOrEqualToThreshold",
                        Threshold=1.0,
                        Period=60 * 60,  # in seconds
                        EvaluationPeriods=2,
                        Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
                        Unit="Percent",
                        ActionsEnabled=True,
                        AlarmActions=[
                            ":".join(
                                [
                                    "arn:aws:swf",
                                    region,
                                    account_id,
                                    "action/actions/AWS_EC2.InstanceId.Stop/1.0",
                                ]
                            )
                        ],
                    )
