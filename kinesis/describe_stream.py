import boto3
from pprint import pprint

kinesis = boto3.client('kinesis')
response = kinesis.describe_stream(StreamName='test')
pprint(response)

# StreamStatus:
# ストリーム作成中の場合は、「CREATING」となります。
# ストリーム作成済み(利用可能)の場合は、「ACTIVE」となります。
# ストリーム削除中の場合は、「DELETING」となります。
# ストリームが完全に削除されると、(指定されたストリームが存在しないため)エラーとなります。