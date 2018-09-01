import boto3
from pprint import pprint

sns = boto3.resource('sns')
topic = sns.create_topic(Name='test')
pprint(topic)