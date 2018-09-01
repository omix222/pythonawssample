import boto3

dynamodb = boto3.resource('dynamodb')

users = dynamodb.Table('Users')

taro = {
    'Id': 2,
    'Name': 'Taro2',
    'Grougs': ['Admin', 'Developers']
}

users.put_item(Item=taro)