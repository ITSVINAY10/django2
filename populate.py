import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sunnyjobs.settings')
import django
django.setup()

from testapp.models import HydJobs
from faker import Faker
from random import *
faker = Faker()
def phonenumbergen():
	d1 = randint(6,9)
	num = '' + str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)
def populate(n):
	for i in range(n):
		fdate = faker.date()
		fcompany = faker.company()
		ftitle = faker.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
		feligibility = faker.random_element(elements=('B.Tech','M.Tech','MCA','Mahesh Sir Student'))
		femail = faker.email()
		faddress = faker.address()
		fphonenumber = phonenumbergen()
		hyd_jobs_record = HydJobs.objects.get_or_create(
			date = fdate,
			company = fcompany,
			title = ftitle,
			eligibility = feligibility,
			email = femail,
			address=faddress,
			phonenumber = fphonenumber
			)
n = int(input('Enter number of records:'))
populate(n)
print('{n} Records inserted successfully......')
 