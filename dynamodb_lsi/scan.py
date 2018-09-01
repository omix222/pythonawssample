import boto3
from pprint import pprint

client = boto3.client('dynamodb')

response = client.scan(
    TableName='Files',
    IndexName='FilesBySize'
)
pprint(response)