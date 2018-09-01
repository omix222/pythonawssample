import boto3
from pprint import pprint

kinesis = boto3.client('kinesis')
response = kinesis.put_record(StreamName='test', Data='helloこんにちはww', PartitionKey='1')
pprint(response)