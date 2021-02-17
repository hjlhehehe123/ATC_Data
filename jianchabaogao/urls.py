from django.conf.urls import url
from . import views

urlpatterns = [
#检查报告
url(r'^showjianchabaogao/$', views.showjianchabaogao, name="showjianchabaogao"),
url(r'^addjianchabaogao/$', views.addjianchabaogao, name="addjianchabaogao"),
url(r'^indexjianchabaogao/$', views.indexjianchabaogao, name="indexjianchabaogao"),
url(r'^find/$', views.find, name="find"),

]