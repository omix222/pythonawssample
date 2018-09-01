import boto3
from pprint import pprint

dynamodb = boto3.resource('dynamodb')

users = dynamodb.Table('Users')

response = users.query(
    KeyConditionExpression='Id = :id',
    # :idで仮の値で初期化。以下で上書き。Prepared Statementっぽい。上記で値を入れるのはNG
    ExpressionAttributeValues={':id': 1}
)

pprint(response)