import boto3
from pprint import pprint

dynamodb = boto3.resource('dynamodb')

users = dynamodb.Table('Users')

response = users.scan()

pprint(response)

# Items: スキャンされた項目のリスト
# ScannedCount - フィルタ式 (存在する場合) が適用される前に、キー条件式に一致する項目数。
# Count - フィルタ式 (存在する場合) が適用された後、残っている項目数。