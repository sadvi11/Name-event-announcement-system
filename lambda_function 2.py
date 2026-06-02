import json
import boto3
import os

sns = boto3.client('sns', region_name='ca-central-1')
TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN', '')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        title = body.get('title', 'No Title')
        message = body.get('message', 'No Message')
        sender = body.get('email', 'anonymous')

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject=f"Event Announcement: {title}",
            Message=f"Event: {title}\n\nDescription: {message}\n\nSent by: {sender}"
        )

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Announcement sent', 'status': 'success'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
