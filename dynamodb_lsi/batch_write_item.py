import boto3
from pprint import pprint

client = boto3.client('dynamodb')

items = [
    {'Folder': {'S': '/Users/taro/Documents'}, 'File': {'S': 'memo.txt'}, 'Comment': {'S': 'メモ(Document)'},
     'Size': {'N': '101'}},
    {'Folder': {'S': '/Users/taro/Documents'}, 'File': {'S': 'memo_bak.txt'}, 'Comment': {'S': 'メモ(Document)'},
     'Size': {'N': '101'}},
    {'Folder': {'S': '/Users/taro/Documents'}, 'File': {'S': 'task.txt'}, 'Comment': {'S': 'タスクリスト'},
     'Size': {'N': '1234'}},
    {'Folder': {'S': '/Users/taro/Documents'}, 'File': {'S': 'app.py'}, 'Comment': {'S': '練習プログラム'},
     'Size': {'N': '567'}},
    {'Folder': {'S': '/Users/taro/Documents'}, 'File': {'S': 'meeting.docx'}, 'Comment': {'S': '議事録'},
     'Size': {'N': '34567'}},
    {'Folder': {'S': '/Users/taro/Pictures'}, 'File': {'S': 'memo.txt'}, 'Comment': {'S': 'メモ(Pictures)'},
     'Size': {'N': '202'}},
    {'Folder': {'S': '/Users/taro/Pictures'}, 'File': {'S': 'logo_new.png'}, 'Comment': {'S': '旧ロゴ画像'},
     'Size': {'N': '89012'}},
    {'Folder': {'S': '/Users/taro/Pictures'}, 'File': {'S': 'logo_old.png'}, 'Comment': {'S': '新ロゴ画像'},
     'Size': {'N': '67890'}},
    {'Folder': {'S': '/Users/taro/Downloads'}, 'File': {'S': 'memo.txt'}, 'Comment': {'S': 'メモ(Downloads)'},
     'Size': {'N': '202'}},
]

response = client.batch_write_item(
    RequestItems={
        'Files': [{'PutRequest': {'Item': item}} for item in items]
    }
)

pprint(response)