"""ATC_Data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import *
from . import view,testdb

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]
"""

import pymysql

pymysql.version_info = (1, 3, 13, "final", 0)

pymysql.install_as_MySQLdb()

from django.conf.urls import url, include
from django.urls import path

from ATC_Data import view

urlpatterns = [
    url(r'^$', view.login),

    path('banzu/', view.banzu, name="banzu"),
    path('instruction/', view.instruction, name="instruction"),
    path('simulator/', view.simulator, name="simulator"),
    path('closedtrainning/', view.closedtrainning, name="closedtrainning"),
    path('ontrainning/', view.ontrainning, name="ontrainning"),
    path('sheet/', view.sheet, name="sheet"),
    path('analysis/', view.analysis, name="analysis"),
    path('makeplan/', view.makeplan, name="makeplan"),

    path('getsheet/', view.getsheet, name="getsheet"),
    # path('getinfo/', view.getinfo, name="getinfo"),
    path('saveevaluationresult/', view.saveevaluationresult, name="saveevaluationresult"),
    # path('^ajax/',ajax),
    url(r'^TestModel/', include('TestModel.urls')),
    url(r'^atcInfo/', include('atcInfo.urls')),
    url(r'^trainningcompletion/', include('trainningcompletion.urls')),
    url(r'^data_anaiysis/', include('data_anaiysis.urls')),
    url(r'^xunliankaohe/', include('xunliankaohe.urls')),
    url(r'^jianchabaogao/', include('jianchabaogao.urls')),
    # url('getinfo/', view.getinfo, name="getinfo"),

]
