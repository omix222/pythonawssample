import boto3
from pprint import pprint

sns = boto3.resource('sns')
arn = 'arn:aws:sns:ap-northeast-1:415551984968:test'  # create_topicで表示されたarnを記入してください
topic = sns.Topic(arn)
response = topic.publish(Message='helloこんにちは')
pprint(response)