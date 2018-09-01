import boto3
from pprint import pprint

client = boto3.client('dynamodb')

response = client.query(
    TableName='Files',
    IndexName='FilesBySize',
    KeyConditionExpression='Folder = :f',
    ExpressionAttributeValues={':f': {'S': '/Users/taro/Documents'}}
)
pprint(response['Items'])