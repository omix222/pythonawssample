import boto3

s3 = boto3.resource('s3')

bucket_name = 'test-342432422384973435'    # 数字部分は、create_bucket.pyと同じものを指定
bucket = s3.Bucket(bucket_name)

bucket.put_object(
    Key='test.txt',
    Body='helloこんにちは',
    ServerSideEncryption='AES256'
)