import csv
from faker import Faker
from create_bucket import s3_client
from create_bucket import bucket_name

# # faker is a python library used to generate fake datas
faker = Faker(['en_US',
               'fr_FR'])  # 'Instantiating the faker class,the passed in argument is for locale selection (US & FRANCE in this case), optional, default is en_US'
#
data = []  # 'list to contain generated data'

for i in range(1, 1001):    # '1000 data to be generated
  data.append([i, faker.name(), faker.address(), faker.city(), faker.job(), faker.country(), faker.phone_number()])
  i += 1

# 'Writing data to csv file'
file_name = 'file100.csv'
with open(file_name, 'w') as outfile:
  writer = csv.writer(outfile)
  writer.writerow(['ID_NO', 'NAME', 'ADDRESS', 'CITY', 'JOB', 'COUNTRY', 'PHONE'])  # 'Providing header row'
  writer.writerows(data)

# 'Uploading to s3, path ('/') is only needed if you want to include subdirectory'
s3_file = f'folder/sub-folder/{file_name}'
upload = s3_client.upload_file('file100.csv', bucket_name, s3_file)
print(f'{file_name} has been successfully uploaded to bucket name-- {bucket_name}')

