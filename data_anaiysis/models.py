from django.db import models

# Create your models here.
# python manage.py makemigrations data_anaiysis
# python manage.py migrate data_anaiysis
# Create your models here.
# python manage.py makemigrations sessions
# python manage.py migrate sessions
class tower_trainning_total_time(models.Model):#模拟机培训学时（塔台）
    data01 = models.CharField(max_length=300)  # 年份
    data02 = models.CharField(max_length=300)  # 月份
    data03 = models.CharField(max_length=300)  # 上岗前培训 学时
    data04 = models.CharField(max_length=300)  # 上岗前培训 人次
    data05 = models.CharField(max_length=300)  # 资格培训    学时
    data06 = models.CharField(max_length=300)  # 资格培训    人次
    data07 = models.CharField(max_length=300)  # 复习培训
    data08 = models.CharField(max_length=300)  #
    data09 = models.CharField(max_length=300)  #
    data10 = models.CharField(max_length=300)  #
    data11 = models.CharField(max_length=300)  #
    data12 = models.CharField(max_length=300)  #
    data13 = models.CharField(max_length=300)  #
    data14 = models.CharField(max_length=300)  #
    data15 = models.CharField(max_length=300)  #
    data16 = models.CharField(max_length=300)  #
    data17 = models.CharField(max_length=300)  #
    data18 = models.CharField(max_length=300)  #
    data19 = models.CharField(max_length=300)  #
    data20 = models.CharField(max_length=300)  #
    data21 = models.CharField(max_length=300)  #
    data22 = models.CharField(max_length=300)  #
    data23 = models.CharField(max_length=300)  #
    data24 = models.CharField(max_length=300)  #
    data25 = models.CharField(max_length=300)  #
    data26 = models.CharField(max_length=300)  #
    data27 = models.CharField(max_length=300)  #
    data28 = models.CharField(max_length=300)  #
    data29 = models.CharField(max_length=300)  #
    data30 = models.CharField(max_length=300)  #


class area_trainning_total_time(models.Model):  # 模拟机培训学时（塔台）
        data01 = models.CharField(max_length=300)  # 月份
        data02 = models.CharField(max_length=300)  # 上岗前培训 学时
        data03 = models.CharField(max_length=300)  # 上岗前培训 人次
        data04 = models.CharField(max_length=300)  # 资格培训    学时
        data05 = models.CharField(max_length=300)  # 资格培训    人次
        data06 = models.CharField(max_length=300)  # 复习培训
        data07 = models.CharField(max_length=300)  #
        data08 = models.CharField(max_length=300)  #
        data09 = models.CharField(max_length=300)  #
        data10 = models.CharField(max_length=300)  #
        data11 = models.CharField(max_length=300)  #
        data12 = models.CharField(max_length=300)  #
        data13 = models.CharField(max_length=300)  #
        data14 = models.CharField(max_length=300)  #
        data15 = models.CharField(max_length=300)  #
        data16 = models.CharField(max_length=300)  #
        data17 = models.CharField(max_length=300)  #
        data18 = models.CharField(max_length=300)  #
        data19 = models.CharField(max_length=300)  #
        data20 = models.CharField(max_length=300)  #
        data21 = models.CharField(max_length=300)  #
        data22 = models.CharField(max_length=300)  #
        data23 = models.CharField(max_length=300)  #
        data24 = models.CharField(max_length=300)  #
        data25 = models.CharField(max_length=300)  #
        data26 = models.CharField(max_length=300)  #
        data27 = models.CharField(max_length=300)  #
        data28 = models.CharField(max_length=300)  #
        data29 = models.CharField(max_length=300)  #
        data30 = models.CharField(max_length=300)  #

class instructor_total_time(models.Model):  # 教员教学学时统计
    data26 = models.CharField(max_length=300)  #
    data27 = models.CharField(max_length=300)  #
    data01 = models.CharField(max_length=300)  # 年份
    data02 = models.CharField(max_length=300)  # 月份
    data03 = models.CharField(max_length=300)  #  姓名
    data04 = models.CharField(max_length=300)  #  科室
    data05 = models.CharField(max_length=300)  #
    data06 = models.CharField(max_length=300)  #
    data07 = models.CharField(max_length=300)  #
    data08 = models.CharField(max_length=300)  #
    data09 = models.CharField(max_length=300)  #
    data10 = models.CharField(max_length=300)  #
    data11 = models.CharField(max_length=300)  #
    data12 = models.CharField(max_length=300)  #
    data13 = models.CharField(max_length=300)  #
    data14 = models.CharField(max_length=300)  #
    data15 = models.CharField(max_length=300)  #
    data16 = models.CharField(max_length=300)  #
    data17 = models.CharField(max_length=300)  #
    data18 = models.CharField(max_length=300)  #
    data19 = models.CharField(max_length=300)  #
    data20 = models.CharField(max_length=300)  #
    data21 = models.CharField(max_length=300)  #
    data22 = models.CharField(max_length=300)  #
    data23 = models.CharField(max_length=300)  #
    data24 = models.CharField(max_length=300)  #
    data25 = models.CharField(max_length=300)  #

    data28 = models.CharField(max_length=300)  #
    data29 = models.CharField(max_length=300)  #
    data30 = models.CharField(max_length=300)  #