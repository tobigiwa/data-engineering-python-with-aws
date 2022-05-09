from create_bucket import s3_resource
from create_bucket import bucket_name

# 'Printing objects in bucket before deleting
bucket = s3_resource.Bucket(bucket_name)
for contents in bucket.objects.all():
    print(f'Bucket objects BEFORE DELETING-- {contents.key}')

# 'Print the list of bucket in AWS account using the boto3.resource'
resource_response = s3_resource.buckets.all()
buckets_from_boto3_resource = [bucket.name for bucket in resource_response]
print(f'Bucket names given by the boto3.resource service BEFORE DELETING--{buckets_from_boto3_resource}, count is {len(buckets_from_boto3_resource)} buckets')

def cleanup_s3_bucket():
    #  'Deleting objects in folder'
    for content in bucket.objects.all():
        content.delete()
    # 'Deleting object versions if s3 versioning is enabled'
    for content in bucket.object_versions.all():
        content.delete()

cleanup_s3_bucket()
bucket.delete()

# 'Print the list of bucket in AWS account using the boto3.resource'
resource_response = s3_resource.buckets.all()
buckets_from_boto3_resource = [bucket.name for bucket in resource_response]
print(f'Bucket names given by the boto3.resource service AFTER DELETING--{buckets_from_boto3_resource}, count is {len(buckets_from_boto3_resource)} buckets')

