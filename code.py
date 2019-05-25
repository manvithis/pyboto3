import os
import boto3
import time
from random import random

arr=[]
arr=os.listdir('textfiles')
print(arr)

s3=boto3.resource('s3',aws_access_key_id='',aws_secret_access_key= '')
buckets=s3.buckets.all()
for bucket in buckets:
	print (bucket.name)
for files in arr:
	time.sleep(100 * 5 * 60)
	s3.upload_file(files)
