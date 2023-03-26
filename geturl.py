import os
import boto3
from botocore.exceptions import ClientError
from http import HTTPStatus

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['URLS_TABLE_NAME'])

def handler(event, context):
    print(event)
    short_id = event['path']['id']
    print ("shortid: ", short_id)
    
    try:
        long_url = get_long_url(short_id)
        print("long_url: ",long_url)
        
        if long_url:
            response = {
                'statusCode': 302,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Location': long_url
                    
                },
                'body': ""
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
        print ("long_url_func: ",response['Item']['original_url'])
        return response['Item']['original_url']
    except KeyError:
        return None
    except Exception as e:
        raise ClientError(e)
