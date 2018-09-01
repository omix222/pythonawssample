import boto3
import time

kinesis = boto3.client('kinesis')

# ストリーム内のシャードをリストアップする
response = kinesis.list_shards(StreamName='test')

# シャードIDを取得する。今回のサンプルでは、シャードは1つだけと仮定している。
shardId = response['Shards'][0]['ShardId']

# シャードのレコードを読み取るための「シャードイテレータ」を取得する。
response = kinesis.get_shard_iterator(
    StreamName='test',
    ShardId=shardId,
    ShardIteratorType='TRIM_HORIZON'  # レコードに残っている最古のデータから読み取りを開始
)

shardIterator = response['ShardIterator']

# 無限ループで、レコードを取り出していく。終了するには画面左側の赤い「■」をクリック。
while True:
    # シャードイテレータを指定して、レコードを取り出す。
    response = kinesis.get_records(ShardIterator=shardIterator)

    # get_recordsは、新しいシャードイテレータ(NextShardIterator)を返す。
    # 次回のget_recordsでは、この新しいシャードイテレータを使用する。
    shardIterator = response['NextShardIterator']

    # レスポンスに含まれるレコードの件数が0件？
    if len(response['Records']) == 0:
        # 0件の場合は、1秒スリープ
        time.sleep(1)
    else:
        # 1件以上の場合。各レコードの内容を表示
        for record in response['Records']:
            print('PartitionKey:', record['PartitionKey'])
            print('SequenceNumber', record['SequenceNumber'])
            print('Data:', record['Data'].decode())
            print('---')