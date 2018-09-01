import boto3
from pprint import pprint

sqs = boto3.resource('sqs')

# 名前を指定して、既存のキューを取得
queue = sqs.get_queue_by_name(QueueName='test')
pprint(queue)

# URLを指定して、既存のキューを取得することもできる。
# queue = sqs.Queue('https://ap-northeast-1.queue.amazonaws.com/408530216586/test')
# pprint(queue)