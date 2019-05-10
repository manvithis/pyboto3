import os
import boto3
arr=[]
arr=os.listdir('textfiles')
print(arr)

s3=boto3.resource('s3',aws_access_key_id='',aws_secret_access_key= '')
buckets=s3.buckets.all()
for bucket in buckets:
	print (bucket.name)