#from django.db import models

# Create your models here.
# models.py
# python manage.py makemigrations atcinfo
# python manage.py migrate atcinfo
# atcinfo trainningcompletion
from django.db import models


class logins(models.Model):
    atcAccount = models.CharField(max_length=18)
    atcPassword = models.CharField(max_length=8)