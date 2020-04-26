from django.db import models
# python manage.py makemigrations atcInfo
# python manage.py migrate atcInfo
# Create your models here.

class info(models.Model):
    atcName = models.CharField(max_length=20)
    atcOld = models.CharField(max_length=3)