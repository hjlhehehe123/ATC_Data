from django.conf.urls import url

from . import views

urlpatterns = [

    url('getsheet/$', views.getsheet, name="getsheet"),
    # 复训考核表
    url(r'^addjichangfxkhb/$', views.addjichangfxkhb, name="addjichangfxkhb"),
    url(r'^addACCfxkhb/$', views.addACCfxkhb, name="addACCfxkhb"),
    url(r'^addAPPfxkhb/$', views.addAPPfxkhb, name="addAPPfxkhb"),
    #岗前
    url(r'^addACCgqkhb/$', views.addACCgqkhb, name="addACCgqkhb"),
    url(r'^addAPPgqkhb/$', views.addAPPgqkhb, name="addAPPgqkhb"),
    url(r'^addjichanggqkhb/$', views.addjichanggqkhb, name="addjichanggqkhb"),

]
