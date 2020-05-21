from django.db import models


# python manage.py makemigrations atcInfo
# python manage.py migrate atcInfo
# Create your models here.

class info(models.Model):
    atcName = models.CharField(max_length=20)
    atcOld = models.CharField(max_length=3)


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


class trainningstatusdetail(models.Model):
    frontdata1 = models.CharField(max_length=300)
    frontdata2 = models.CharField(max_length=300)
    frontdata3 = models.CharField(max_length=300)
    frontdata4 = models.CharField(max_length=300)
    frontdata5 = models.CharField(max_length=300)
    frontdata6 = models.CharField(max_length=300)
    frontdata7 = models.CharField(max_length=300)
    frontdata8 = models.CharField(max_length=300)
    frontdata9 = models.CharField(max_length=300)
    frontdata10 = models.CharField(max_length=300)
    frontdata11 = models.CharField(max_length=300)
    frontdata12 = models.CharField(max_length=300)
    frontdata13 = models.CharField(max_length=300)
    frontdata14 = models.CharField(max_length=300)
    frontdata15 = models.CharField(max_length=300)
    frontdata16 = models.CharField(max_length=300)


class saveevaluationresult(models.Model):
    score = models.CharField(max_length=300)
    训练情况 = models.CharField(max_length=300)
    教员评语 = models.CharField(max_length=300)
    studentname = models.CharField(max_length=300)
    teachername = models.CharField(max_length=300)
    selLocation11 = models.CharField(max_length=300)
