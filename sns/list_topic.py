import boto3
from pprint import pprint

sns = boto3.resource('sns')
for topic in sns.topics.all():
    pprint(topic)