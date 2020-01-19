import boto3
import functools
import sys

REGION = 'us-east-1'




def log_event_on_error(handler):
    @functools.wraps(handler)
    def wrapper(event, context):
        try:
            return handler(event, context)
        except Exception:
            print('event = %r' % event)
            raise

    return wrapper

@log_event_on_error
def lambda_handler(event, context):
    print(0)
    ec2 = boto3.resource('ec2', region_name=REGION)
    print(1)
    for instance in ec2.instances.all():
        print(2)
        print(instance)
        print(3)
        ec2_cl = boto3.client('ec2', REGION)
        ec2_cl.terminate_instances(InstanceIds=[instance.id])
        print("Stoped\n\n")




