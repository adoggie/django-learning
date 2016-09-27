"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

import Jomo
from Jomo.views import RedisTestView
from Jomo import rest_views

urlpatterns = [
    url(r'^redis/$', RedisTestView.as_view(),name='redis_test'),
    url(r'^rest/test/$', rest_views.TestListView.as_view(),name='rest_test'),
    url(r'^rest/test2/$', rest_views.TestDBTableView.as_view(),name='rest_test2'),
    url(r'^easyui/test/$',TemplateView.as_view(template_name='Jomo/test_easyui.html'),name='easyui')

]
