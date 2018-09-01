import boto3
from pprint import pprint

s3 = boto3.resource('s3', region_name='ap-northeast-1')

while True:
    command = input('コマンド: ')
    if command == 'create bucket':
        bucket = input('バケット名: ')
        print('バケット %s を作成します' % bucket)
        response=s3.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-northeast-1'
            }
        )
        pprint(response)
    elif command == 'delete bucket':
        bucket = input('バケット名: ')
        print('バケット %s を削除します' % bucket)
        response=s3.Bucket(bucket).delete()
        pprint(response)
    elif command == 'put object':
        bucket = input('バケット名: ')
        key = input('キー: ')
        content = input('内容: ')
        print('バケット{}、キー{}のオブジェクトを作成し、内容{}を書き込みます。', bucket, key, content)
        bucket_obj = s3.Bucket(bucket)
        response = bucket_obj.put_object(
            Key=key,
            Body=content
        )
        pprint(response)
    elif command == 'get object':
        bucket = input('バケット名: ')
        key = input('キー: ')
        print('指定したバケット内の特定のキーのオブジェクトの内容を表示します。', bucket, key)
        bucket_obj = s3.Object(bucket, key)
        print(bucket_obj.key)
        obj_body = bucket_obj.get()
        body = obj_body['Body'].read()
        print(body.decode('utf-8'))
    elif command == 'list object':
        bucket = input('バケット名: ')
        print('指定したバケット内のオブジェクト一覧を表示します。', bucket)
        bucket_obj = s3.Bucket(bucket)
        for obj in bucket_obj.objects.all():
            print(obj.key)
            obj_body = obj.get()
            body = obj_body['Body'].read()
            print(body.decode('utf-8'))
    elif command == 'quit' or command == 'exit':
        print('終了します')
        break