import os
import boto3
from botocore.exceptions import ClientError
from http import HTTPStatus

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['URLS_TABLE_NAME'])

def handler(event, context):
    short_id = event['pathParameters']['id']
    try:
        long_url = get_long_url(short_id)
        html_body = f"""
             <!DOCTYPE html>
             <html>
             <head>
                 <meta http-equiv="refresh" content="0;url={long_url}" />
                 <script>
                     window.location.href = '{long_url}';
                 </script>
             </head>
             <body>
             </body>
             </html>
             """
        
        if long_url:
            response = {
                'statusCode': 302,
                'headers': {
                    'Content-Type': 'text/html',
                    'Access-Control-Allow-Origin': '*'
                    
                    
                },
                'body': html_body
            }
        else:
            response = {
                'statusCode': HTTPStatus.NOT_FOUND,
                'body': 'Short URL not found'
            }
    
    except ClientError as e:
        response = {
            'statusCode': HTTPStatus.INTERNAL_SERVER_ERROR,
            'body': f'Error fetching URL: {str(e)}'
        }
    print (response)
    return response

def get_long_url(short_id):
    try:
        response = table.get_item(Key={'id': short_id})
        return response['Item']['original_url']
    except KeyError:
        return None
    except Exception as e:
        raise ClientError(e)
