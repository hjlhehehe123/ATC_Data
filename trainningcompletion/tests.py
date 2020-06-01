from django.test import TestCase

# Create your tests here.
from datetime import datetime

now_time = datetime.now()
month = datetime.strftime(now_time, "%m")
data03 = month + "月"
print(data03)

