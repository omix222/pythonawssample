import boto3

s3 = boto3.resource('s3', region_name='ap-northeast-1')

bucket_name = 'test-342432422384973435'  # 数字部分は適当に書き換えてください

s3.Bucket(bucket_name).delete()