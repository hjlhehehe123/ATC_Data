from django.db import models


# python manage.py makemigrations xunliankaohe
# python manage.py migrate xunliankaohe
# Create your models here.
# python manage.py makemigrations sessions
# python manage.py migrate sessions
# Create your models here.
class jichangfxkhb(models.Model):
    frontdata1 = models.CharField(max_length=100)  # 姓名
    frontdata2 = models.CharField(max_length=30)  # 间隔次数
    frontdata3 = models.CharField(max_length=30)  # 间隔扣分
    frontdata4 = models.CharField(max_length=500)  # 具体扣分项
    frontdata5 = models.CharField(max_length=30)  # 协调
    frontdata6 = models.CharField(max_length=30)
    frontdata7 = models.CharField(max_length=500)
    frontdata8 = models.CharField(max_length=30)  # 意识
    frontdata9 = models.CharField(max_length=30)
    frontdata10 = models.CharField(max_length=500)
    frontdata11 = models.CharField(max_length=30)  # 陆空通话
    frontdata12 = models.CharField(max_length=30)
    frontdata13 = models.CharField(max_length=500)
    frontdata14 = models.CharField(max_length=30)  # 特情
    frontdata15 = models.CharField(max_length=30)
    frontdata16 = models.CharField(max_length=500)
    frontdata17 = models.CharField(max_length=30)  # 雷达
    frontdata18 = models.CharField(max_length=30)
    frontdata19 = models.CharField(max_length=500)
    frontdata20 = models.CharField(max_length=30)  # 其他扣分数
    frontdata21 = models.CharField(max_length=500)  # 其他扣分具体项
    frontdata22 = models.CharField(max_length=30)  # 是否通过
    frontdata23 = models.CharField(max_length=30)  # 总分
