# from parent lambda a child lambda is invoked

import json

def lambda_handler(event, context):
    
    import boto3
    from botocore.exceptions import NoCredentialsError

    
    # Plugging in credentials
    ACCESS_KEY = 'XXXXXX'                         
    SECRET_KEY = 'XXXXX'
    s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    lambda_client = boto3.client('lambda',region_name='us-west-1')
    
    # Declare payload
    event_payload ={}
    
    event_payload['key-1'] = "Value 1"
    event_payload['key-2'] = "Value 2"
    event_payload['key-3'] = "Value 3"
    
    
    lambda_client.invoke(FunctionName='arn:aws:lambda:us-west-1:XXXXXXXXXX',InvocationType='Event',Payload= json.dumps(event_payload))
        
            

    return {
        'statusCode': 200,
        'body': 'Child Lambda got invoked'
    }
