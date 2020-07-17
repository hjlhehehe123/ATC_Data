from django.conf.urls import url
from . import views

urlpatterns = [
# 模拟机培训学时（塔台）
url(r'^tower_trainning_total_time/$', views.tower_trainning_total_time, name="tower_trainning_total_time"),
url(r'^tower_trainning_total_time_post/$', views.tower_trainning_total_time_post, name="tower_trainning_total_time_post"),
url(r'^test/$', views.test, name="test"),


# 教员教学学时统计
url(r'^instructor_total_time/$', views.instructor_total_time, name="instructor_total_time"),
url(r'^instructor_total_time_post/$', views.instructor_total_time_post, name="instructor_total_time_post"),
url(r'^test/$', views.test, name="test"),




# 教员列表
url(r'^instructor_teach_record_instructorlist/$',
    views.instructor_teach_record_instructorlist,
    name="instructor_teach_record_instructorlist"),
url(r'^instructor_teach_record_instructorlist_post/$',
    views.instructor_teach_record_instructorlist_post,
    name="instructor_teach_record_instructorlist_post"),
# 教员教学记录
url(r'^instructor_teach_record/$',
    views.instructor_teach_record,
    name="instructor_teach_record"),
url(r'^instructor_teach_record_post/$',
    views.instructor_teach_record_post,
    name="instructor_teach_record_post"),
url(r'^test/$', views.test, name="test"),






]
