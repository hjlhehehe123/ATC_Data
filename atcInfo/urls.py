from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getinfo/$', views.getinfo, name='getinfo'),
    url(r'^trainningstatus/$', views.gettrainningstatus, name='trainningstatus'),
    url(r'^infosearch/$', views.infosearch, name='infosearch'),

    url(r'^getinfo_save/$', views.getinfo_save, name='getinfo_save'),
    url(r'^getinfo_save_ajax/$', views.getinfo_save_ajax, name='getinfo_save_ajax'),
    url(r'^getinfo_input/$', views.getinfo_input, name='getinfo_input'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^download/$', views.download, name='download'),

    # url(r'^getinfo_save_01/$', views.getinfo_save_01, name='getinfo_save_01'),
    # url(r'^getinfo_save_02/$', views.getinfo_save_02, name='getinfo_save_02'),
    # url(r'^getinfo_save_03/$', views.getinfo_save_03, name='getinfo_save_03'),
    # url(r'^getinfo_save_04/$', views.getinfo_save_04, name='getinfo_save_04'),
    # url(r'^getinfo_save_05/$', views.getinfo_save_05, name='getinfo_save_05'),
    # url(r'^getinfo_save_06/$', views.getinfo_save_06, name='getinfo_save_06'),
    # url(r'^getinfo_save_07/$', views.getinfo_save_07, name='getinfo_save_07'),
    # url(r'^getinfo_save_08/$', views.getinfo_save_08, name='getinfo_save_08'),
    # url(r'^getinfo_save_09/$', views.getinfo_save_09, name='getinfo_save_09'),
    # url(r'^getinfo_save_10/$', views.getinfo_save_10, name='getinfo_save_10'),
    # url(r'^getinfo_save_11/$', views.getinfo_save_11, name='getinfo_save_11'),
    # url(r'^getinfo_save_12/$', views.getinfo_save_12, name='getinfo_save_12'),
    # url(r'^getinfo_save_13/$', views.getinfo_save_13, name='getinfo_save_13'),
    # url(r'^getinfo_save_14/$', views.getinfo_save_14, name='getinfo_save_14'),
    # url(r'^getinfo_save_15/$', views.getinfo_save_15, name='getinfo_save_15'),
    # url(r'^getinfo_save_16/$', views.getinfo_save_16, name='getinfo_save_16'),
    # url(r'^getinfo_save_17/$', views.getinfo_save_17, name='getinfo_save_17'),
    # url(r'^getinfo_save_18/$', views.getinfo_save_18, name='getinfo_save_18'),
]
