import configparser
import csv
import boto3
from faker import Faker

# faker is a python library used to generate fake datas
faker = Faker(['en_US',
               'fr_FR'])  # 'Instantiating the faker class,the passed in argument is for locale selection (US & FRANCE in this case), optional, default is en_US'

data = []  # 'list to contain generated data'

for i in range(1, 1001):    # '1000 data to be generated(name, address, city, job, country, phone_number)'
    data.append([i, faker.name(), faker.address(), faker.city(), faker.job(), faker.country(), faker.phone_number()])
    i += 1

# print(data)   # ' to view data in terminal'

# 'Writing data to csv file'
with open('file100.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['ID_NO', 'NAME', 'ADDRESS', 'CITY', 'JOB', 'COUNTRY', 'PHONE']) # 'Providing header row'
    writer.writerows(data)


# # 'Accessing s3 Login credentials with configparser'
parser = configparser.ConfigParser()
parser.read("connection.conf")
access_key = parser.get('aws_boto_credentials', 'access_key')
secret_key = parser.get('aws_boto_credentials', 'secret_key')
bucket_name = parser.get('aws_boto_credentials', 'bucket_name')

# # 'Connecting to s3'
s3 = boto3.client('s3', aws_access_key_id=access_key,
                  aws_secret_access_key=secret_key)

# # 'Uploading to s3, path ('/') is only needed if you want to include subdirectory'
s3_file = 'folder/sub-folder/file100.csv'
s3.upload_file('file100.csv', bucket_name, s3_file)
