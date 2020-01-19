import boto3

REGION = 'us-east-1'


def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name=REGION)
    for instance in ec2.instances.all():
        print(instance)
        ec2_cl = boto3.client('ec2', REGION)
        ec2_cl.stop_instances(InstanceIds=[instance.id])
        print("Stoped\n\n")



