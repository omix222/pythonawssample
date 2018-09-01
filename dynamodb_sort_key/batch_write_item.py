import boto3
from pprint import pprint

dynamodb = boto3.resource('dynamodb')

response = dynamodb.batch_write_item(
    RequestItems={  # batch_write_itemとbatch_get_itemには、RequestItemsを指定。
        'Tweets': [  # テーブルを指定
            {'PutRequest': {'Item': {'UserId': 1, 'TweetDate': '2018/01/01', 'TweetText': 'User1 Tweet1'}}},
            {'PutRequest': {'Item': {'UserId': 1, 'TweetDate': '2018/01/02', 'TweetText': 'User1 Tweet2'}}},
            {'PutRequest': {'Item': {'UserId': 1, 'TweetDate': '2018/01/03', 'TweetText': 'User1 Tweet3'}}},
            {'PutRequest': {'Item': {'UserId': 2, 'TweetDate': '2018/01/01', 'TweetText': 'User2 Tweet1'}}},
            {'PutRequest': {'Item': {'UserId': 2, 'TweetDate': '2018/01/02', 'TweetText': 'User2 Tweet2'}}},
        ]
    }
)

pprint(response)