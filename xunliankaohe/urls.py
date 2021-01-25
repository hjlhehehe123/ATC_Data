from django.conf.urls import url

from . import views

urlpatterns = [

    # 复训考核表
    url(r'^addjichangfxkhb/$', views.addjichangfxkhb, name="addjichangfxkhb"),

]
