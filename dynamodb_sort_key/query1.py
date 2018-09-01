import boto3
from pprint import pprint

dynamodb = boto3.resource('dynamodb')

tweets = dynamodb.Table('Tweets')

response = tweets.query(
    KeyConditionExpression='UserId = :uid',
    ExpressionAttributeValues={':uid': 1}
)

pprint(response)  # レスポンスの Items を確認。 TweetDateの昇順（つぶやきが新しい順）に並ぶ。