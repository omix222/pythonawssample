import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='test')

# キューにメッセージを送信する
queue.send_message(MessageBody='helloこんにちは')