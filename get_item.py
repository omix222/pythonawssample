import boto3
from pprint import pprint

dynamodb = boto3.resource('dynamodb')

users = dynamodb.Table('Users')

response = users.get_item(Key={'Id': 1})

pprint(response)