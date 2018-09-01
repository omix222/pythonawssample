import boto3
from pprint import pprint

sns = boto3.resource('sns')
arn = 'arn:aws:sns:ap-northeast-1:408530216586:test'  # create_topicで表示されたarnを記入してください
topic = sns.Topic(arn)
topic.delete()