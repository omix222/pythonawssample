import boto3
from pprint import pprint

dynamodb = boto3.resource('dynamodb')

tweets = dynamodb.Table('Tweets')

response = tweets.query(
    KeyConditionExpression='UserId = :uid',
    ExpressionAttributeValues={':uid': 1},
    ScanIndexForward=False
)

pprint(response)  # レスポンスの Items を確認。 TweetDateの降順（つぶやきが古い順）に並ぶ。