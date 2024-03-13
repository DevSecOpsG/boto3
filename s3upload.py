import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file(r"C:\bin\boto3" , 'elasticbeanstalk-us-east-2-381491904552', 's3upload.py')
