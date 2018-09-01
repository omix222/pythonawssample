import boto3
from pprint import pprint

dynamodb = boto3.resource('dynamodb')

response = dynamodb.create_table(
    TableName='Tweets',
    KeySchema=[
        {'AttributeName': 'UserId', 'KeyType': 'HASH'},
        {'AttributeName': 'TweetDate', 'KeyType': 'RANGE'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'UserId', 'AttributeType': 'N'},
        {'AttributeName': 'TweetDate', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10,
    }
)

pprint(response)