import boto3
from pprint import pprint

client = boto3.client('dynamodb')

# ファイル テーブル Files

# [P]フォルダ ... /Users/taro/Documents など
# [S]ファイル名 ... memo.txt など
# [S]ファイルサイズ ... バイト数
# コメント ... ファイルに対する説明文（任意のテキスト）

# フォルダ+ファイルで一意
# フォルダ指定、ファイル名でソート。... テーブルを使用してクエリ
# フォルダ指定、サイズでソート。 ... ファイルサイズを使用してクエリ

response = client.create_table(
    TableName='Files',
    KeySchema=[
        {'AttributeName': 'Folder', 'KeyType': 'HASH'},
        {'AttributeName': 'File', 'KeyType': 'RANGE'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'Folder', 'AttributeType': 'S'},
        {'AttributeName': 'File', 'AttributeType': 'S'},
        {'AttributeName': 'Size', 'AttributeType': 'N'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10,
    },
    LocalSecondaryIndexes=[
        {
            'IndexName': 'FilesBySize',
            'KeySchema': [
                {'AttributeName': 'Folder', 'KeyType': 'HASH'},
                {'AttributeName': 'Size', 'KeyType': 'RANGE'}
            ],
            'Projection': {
                'ProjectionType': 'ALL',  # INCLUDE, ALL, KEYS_ONLYのいずれか。
                # 'NonKeyAttributes': ['FileType']  # INCLUDEの場合必須。ALL, KEYS_ONLYの場合、指定するとエラー。
            }
        }
    ]
)

pprint(response)