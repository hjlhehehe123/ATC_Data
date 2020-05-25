from django.conf.urls import url
from . import views

urlpatterns=[
    #登陆页面
    url(r'^login/$', views.login, name='login'),
    #登录验证
    url(r'^do_login/$', views.do_login, name='do_login'),
    url(r'^do_logout/$', views.do_logout, name='do_logout'),

]
