import boto3

kinesis = boto3.client('kinesis')
kinesis.create_stream(StreamName='test', ShardCount=1)