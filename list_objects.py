import boto3

s3 = boto3.resource('s3')

bucket_name = 'sample234234242432'  # 数字部分は、create_bucket.pyと同じものを指定

bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.all():
    print(obj.key)
    print(obj.get())