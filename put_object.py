import boto3

s3 = boto3.resource('s3')

bucket_name = 'test-342432422384973435'    # 数字部分は、create_bucket.pyと同じものを指定
bucket = s3.Bucket(bucket_name)

response = bucket.put_object(
    Key='test.txt',
    Body='helloこんにちは'
)

response = s3.meta.client.generate_presigned_url(
    ClientMethod='get_object',
    Params={'Bucket': bucket_name, 'Key': 'test.txt'},
    ExpiresIn=10,
    HttpMethod='GET'
)
print(response)