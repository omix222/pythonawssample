import boto3

kinesis = boto3.client('kinesis')
kinesis.delete_stream(StreamName='test')