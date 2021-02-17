from django.db import models

# Create your models here.
class jianchabaogao(models.Model):
    frontdata1 = models.CharField(max_length=100)  #检查科室
    frontdata2 = models.CharField(max_length=100)  #检查类型
    frontdata3 = models.CharField(max_length=100)  #被检查人
    frontdata4 = models.CharField(max_length=50)  #检查时段开始
    frontdata5 = models.CharField(max_length=50)  #检查时段结束
    frontdata6 = models.CharField(max_length=100)   #关键指标
    frontdata7 = models.CharField(max_length=100)  #评价
    frontdata8 = models.CharField(max_length=1000)  #具体描述