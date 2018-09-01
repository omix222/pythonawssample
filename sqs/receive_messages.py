import boto3
from pprint import pprint

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='test')

# キューからメッセージを受信する
messages = queue.receive_messages()

# 受信したメッセージそれぞれについて処理を行う
for message in messages:
    # メッセージの本文（MessageBody）を取得して表示する
    pprint(message.body)
    # 処理が終わったら、そのメッセージを削除する
    message.delete()