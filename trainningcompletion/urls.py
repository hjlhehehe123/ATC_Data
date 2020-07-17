from django.conf.urls import url
from . import views

urlpatterns = [

# 这是模拟机培训的培训记录
url(r'^addtrainningrecord/$', views.addtrainningrecord, name="addtrainningrecord"),
url(r'^addtrainningrecord1/$', views.addtrainningrecord1, name="addtrainningrecord1"),

url(r'^ajax_addtrainningrecord/$', views.ajax_addtrainningrecord),
url(r'^ajax_addtrainningrecord2/$', views.ajax_addtrainningrecord2),
url(r'^trainningstatusdetail/$', views.trainningstatusdetail, name="trainningstatusdetail"),

url(r'^change_trainning_record/$', views.change_trainning_record, name="change_trainning_record"),
url(r'^change_trainning_record_save/$', views.change_trainning_record_save, name="change_trainning_record_save"),


# 这是其他培训的
url(r'^addtrainningrecordother/$', views.addtrainningrecordother, name="addtrainningrecordother"),
url(r'^addtrainningrecordother1/$', views.addtrainningrecordother1, name="addtrainningrecordother1"),
url(r'^ajax_addother/$', views.ajax_addother),
url(r'^ajax_addtrainningrecordother/$', views.ajax_addtrainningrecordother),

url(r'^trainningstatusdetailother/$', views.trainningstatusdetailother, name="trainningstatusdetailother"),
url(r'^test/$', views.test, name="test"),

url(r'^change_trainning_record_other/$', views.change_trainning_record_other, name="change_trainning_record_other"),
url(r'^change_trainning_record_other_save/$', views.change_trainning_record_other_save, name="change_trainning_record_other_save"),










]
