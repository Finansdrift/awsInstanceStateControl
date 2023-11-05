import boto3
region = 'eu-west-1'
instances = ['your-instance id here',]

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print ('started instances: ' + str(instances))
    
    #If you want to stop an instance, use ec2.stop_instances
