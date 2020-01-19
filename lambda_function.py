import boto3

REGION = 'us-east-1'


def lambda_handler(event, context):
    print(1)

    ec2 = boto3.resource('ec2', region_name=REGION)

    print(ec2.instances.all())
    for instance in ec2.instances.all():
        print(2)
        print(instance)
        print(3)
        ec2_cl = boto3.client('ec2')
        ec2_cl.terminate_instances(InstanceIds=[instance.id])
        print("Stoped\n\n")
