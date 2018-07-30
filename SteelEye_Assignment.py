#!/usr/bin/python
__author__="Vivek"

#Importing packages

import pandas as pd
import boto3
from botocore.client import Config

#AWS credentials

ACCESS_KEY_ID = 'AKIAJPQV6RB6YOEXBJTA'
ACCESS_SECRET_KEY = '1mI0Ru6hrs4AvAHAM2d3U3S/euQgFdayfLcPoDl9'
BUCKET_NAME = 'my-vivek-bucket-test1'

#Reading file using Pandas library just replace filepath as per yours

data = pd.read_excel('/home/vvdntech/Documents/Data_Science/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/ISO10383_MIC.xls',sheet_name=1)

#To get first five data from the Excel sheet
print (data.head())

#Converting to json

data.to_json('json_data_new.json', orient="records")
data = open('json_data_new.json', 'rb')

#Uploading Data to S3

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='json_data_new.json', Body=data)
print ("Done")
