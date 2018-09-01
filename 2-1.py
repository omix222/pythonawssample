import boto3

s3 = boto3.resource('s3', region_name='ap-northeast-1')

# s3.Bucket('test-342432422384973435').upload_file('sample.py', 'sample.py')

s3.Bucket('test-342432422384973435').download_file('sample.py', 'sample_dl.py')

fout = open('sample_dl.py', 'w')
fout.writelines("文字列を書き込む")
fout.close()


