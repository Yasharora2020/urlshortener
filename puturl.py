import os
import json
import boto3
import hashlib
from botocore.exceptions import ClientError
from http import HTTPStatus

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['URLS_TABLE_NAME'])

def handler(event, context):
    body = json.loads(event['body'])
    original_url = body.get('url')

    if not original_url:
        return {
            'statusCode': HTTPStatus.BAD_REQUEST,
            'body': json.dumps({'error': 'Missing URL parameter'})
        }

    short_id = hashlib.md5(original_url.encode('utf-8')).hexdigest()[:6]
    shortened_url = f'https://{event["headers"]["Host"]}/{event["requestContext"]["stage"]}/{short_id}'

    try:
        put_url(short_id, original_url)
    except ClientError as e:
        return {
            'statusCode': HTTPStatus.INTERNAL_SERVER_ERROR,
            'body': json.dumps({'error': f'Error saving URL: {str(e)}'})
        }

    response = {
        'statusCode': HTTPStatus.OK,
        'body': json.dumps({
            'shortened_url': shortened_url,
            'original_url': original_url
        })
    }

    return response

def put_url(short_id, original_url):
    item = {
        'id': short_id,
        'original_url': original_url
    }

    table.put_item(Item=item)
