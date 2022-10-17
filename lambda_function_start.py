# Start EC2 instances

import json
import boto3

def lambda_handler(event, context):

    ec2 = boto3.resource('ec2')

    instances = ec2.instances.filter(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['stopped']},
            {'Name': 'tag:always-running', 'Values': ['no']}
        ])
        
    # Start the instances
    for instance in instances:
        instance.start()
        print('Started instance: ', instance.id)

    return {
        'statusCode': 200,
        'body': json.dumps('Script finished')
    }
