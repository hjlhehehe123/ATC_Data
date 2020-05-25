from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^addtrainningrecord/$', views.addtrainningrecord, name="addtrainningrecord"),
url(r'^addtrainningrecord1/$', views.addtrainningrecord1, name="addtrainningrecord1"),
url(r'^ajax_add/$', views.ajax_add),
url(r'^ajax_addtrainningrecord/$', views.ajax_addtrainningrecord),
url(r'^ajax_addtrainningrecord2/$', views.ajax_addtrainningrecord),
url(r'^trainningstatusdetail/$', views.trainningstatusdetail, name="trainningstatusdetail"),
url(r'^test/$', views.test, name="test"),

]
