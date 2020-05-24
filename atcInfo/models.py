from django.db import models


# python manage.py makemigrations atcInfo
# python manage.py migrate atcInfo
# Create your models here.

class info(models.Model):
    atcName = models.CharField(max_length=20)
    atcOld = models.CharField(max_length=3)
    基本信息 = models.CharField(max_length=300)
    管制员等级信息 = models.CharField(max_length=300)
    执照信息 = models.CharField(max_length=300)
    英语等级信息 = models.CharField(max_length=300)
    非管制学历信息 = models.CharField(max_length=300)
    管制学历信息 = models.CharField(max_length=300)
    管制工作经历信息 = models.CharField(max_length=300)
    体检信息 = models.CharField(max_length=300)
    奖励信息 = models.CharField(max_length=300)
    惩罚信息 = models.CharField(max_length=300)
    管制教员信息 = models.CharField(max_length=300)
    检查员信息 = models.CharField(max_length=300)
    检查员考核信息 = models.CharField(max_length=300)
    赴外培训信息 = models.CharField(max_length=300)
    岗位培训信息 = models.CharField(max_length=300)
    放单考核信息 = models.CharField(max_length=300)
    执照检查信息 = models.CharField(max_length=300)
    爱岗敬业信息 = models.CharField(max_length=300)
    职称信息 = models.CharField(max_length=300)
    特殊技能信息 = models.CharField(max_length=300)
    科室信息 = models.CharField(max_length=300)






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



class saveevaluationresult(models.Model):
    score = models.CharField(max_length=300)
    训练情况 = models.CharField(max_length=300)
    教员评语 = models.CharField(max_length=300)
    studentname = models.CharField(max_length=300)
    teachername = models.CharField(max_length=300)
    selLocation11 = models.CharField(max_length=300)
