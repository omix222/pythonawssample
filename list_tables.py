import boto3

dynamodb = boto3.resource('dynamodb')

response = dynamodb.tables.all()

for table in response:
    print(table)