from django.db import models

# Create your models here.

# python manage.py makemigrations trainningcompletion
# python manage.py migrate trainningcompletion
# Create your models here.
# python manage.py makemigrations sessions
# python manage.py migrate sessions
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
#    frontdata13 = models.CharField(max_length=300)
#    frontdata14 = models.CharField(max_length=300)
    frontdata15 = models.CharField(max_length=300)
    frontdata16 = models.CharField(max_length=300)

    # 这是其他培训的，other表示其他培训
class trainningstatusdetailother(models.Model):
    frontdata1 = models.CharField(max_length=300)
    frontdata2 = models.CharField(max_length=300)
    frontdata3 = models.CharField(max_length=300)
    frontdata4 = models.CharField(max_length=300)
    frontdata5 = models.CharField(max_length=300)
    frontdata6 = models.CharField(max_length=300)
    frontdata7 = models.CharField(max_length=300)
    frontdata8 = models.CharField(max_length=300)
    # frontdata9 = models.CharField(max_length=300)
    frontdata10 = models.CharField(max_length=300)
    frontdata11 = models.CharField(max_length=300)
    frontdata12 = models.CharField(max_length=300)
 #   frontdata13 = models.CharField(max_length=300)
#    frontdata14 = models.CharField(max_length=300)
    frontdata15 = models.CharField(max_length=300)
    frontdata16 = models.CharField(max_length=300)

class monthplan(models.Model):
    month = models.CharField(max_length=300)
    plan = models.CharField(max_length=300)

class banzu(models.Model):
    bzname = models.CharField(max_length=300)
    bzperson = models.CharField(max_length=300)
