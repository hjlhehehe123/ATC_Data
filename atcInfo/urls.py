from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^atcInfo/$', views.getinfo,name='atcInfo'),
    url(r'^trainningstatus/$', views.gettrainningstatus,name='trainningstatus'),
    url(r'^infosearch/$', views.infosearch, name='infosearch'),

]
