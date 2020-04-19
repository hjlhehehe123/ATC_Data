from django.db import models

# Create your models here.

class info(models.Model):
    atcName = models.CharField(max_length=20)
    atcOld = models.CharField(max_length=3)