from django.db import models


# python manage.py makemigrations atcInfo
# python manage.py migrate atcInfo
# Create your models here.


class evalution1(models.Model):
    detailevalution = models.CharField(max_length=300)
    value = models.CharField(max_length=20, )


class evalution2(models.Model):
    detailevalution = models.CharField(max_length=300)
    value = models.CharField(max_length=20, )


class evalution3(models.Model):
    detailevalution = models.CharField(max_length=300)
    value = models.CharField(max_length=20, )


class evalution4(models.Model):
    detailevalution = models.CharField(max_length=300)
    value = models.CharField(max_length=20, )


class evalution5(models.Model):
    detailevalution = models.CharField(max_length=300)
    value = models.CharField(max_length=20, )
