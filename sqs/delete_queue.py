import boto3

sqs = boto3.resource('sqs')

# キューを取得する。
queue = sqs.get_queue_by_name(QueueName='test')

# キューを削除する
queue.delete()

# 削除後、同じ名前のキューの再作成は、60秒後に実施する必要がある。