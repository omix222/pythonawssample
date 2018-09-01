import boto3
from pprint import pprint

sqs = boto3.resource('sqs')

# キューを作成する。QueueNameで、キューの名前を指定する。
response = sqs.create_queue(QueueName='test')
pprint(response)