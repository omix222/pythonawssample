import boto3

dynamodb = boto3.resource('dynamodb')

users = dynamodb.Table('Users')
users.delete()

