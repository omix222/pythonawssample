import boto3

dynamodb = boto3.resource('dynamodb')

dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {'AttributeName': 'Id', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        # Nは数値型を示す
        {'AttributeName': 'Id', 'AttributeType': 'N'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10,
    }
)
