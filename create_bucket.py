import boto3
import configparser

# 'Passing login credentials'
parser = configparser.ConfigParser()
parser.read('connection.conf')
access_key = parser.get('aws_boto3', 'access_key')
secret_key = parser.get('aws_boto3', 'secret_key')
bucket_name = parser.get('aws_boto3', 'bucket')

# 'Creating a boto3 Session'
sess = boto3.Session(aws_access_key_id=access_key,        # 'Login creds from configparser'
                    aws_secret_access_key=secret_key,
                    region_name='eu-west-2')              # 'Optional, if omitted "eu-east-1" is default'

s3_client = sess.client('s3')                             # 'Using the "client" service for low-level API calls'
s3_resource = sess.resource('s3')                         # 'Using the "resource" service in a higher object-oriented way


if __name__ == '__main__':
    # 'Creating S3 bucket using boto3.client, boto3.resource can be used by changing to "s3_resource.create_bucket(...)"'
    create_bucket = s3_client.create_bucket(Bucket=bucket_name,                           # 'bucket name from configparser'
                                                 CreateBucketConfiguration={
                                                     'LocationConstraint': 'eu-west-2'})  # 'bucket preferred location
    # 'Displays bucket  information
    print(f'Bucket process information-- {create_bucket}')

    # 'Print the list of bucket in AWS account using the boto3.client'
    client_response = s3_client.list_buckets()
    buckets_from_boto3_client = [bucket['Name'] for bucket in client_response['Buckets']]
    print(f'Bucket name given by the BOTO3.CLIENT service-- {buckets_from_boto3_client}, count is {len(buckets_from_boto3_client)} buckets')

    # 'Print the list of bucket in AWS account using the boto3.resource'
    resource_response = s3_resource.buckets.all()
    buckets_from_boto3_resource = [bucket.name for bucket in resource_response]
    print(f'Bucket name given by the BOTO3.RESOURCE service--{buckets_from_boto3_resource}, count is {len(buckets_from_boto3_resource)} buckets')







