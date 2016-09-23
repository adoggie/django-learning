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

import  views

urlpatterns = [
    url(r'^$', views.ToolsListView.as_view(),name='tools'),
    url(r'^urlencode/$', views.UrlEncodeView.as_view(),name='tool-urlencode'),
    url(r'^myip/$', views.my_ip,name='tool-myip'),
    # url(r'^base64/$', RedisTestView.as_view(),name='redis_test'),
    # url(r'^md5/$', RedisTestView.as_view(),name='redis_test'),
    # url(r'^rainbow/$', RedisTestView.as_view(),name='redis_test'),
    # url(r'^randpassword/$', RedisTestView.as_view(),name='redis_test'),
    # url(r'^uuid/$', RedisTestView.as_view(),name='redis_test'),
    # url(r'^verify_image/$', RedisTestView.as_view(),name='redis_test'),
    # url(r'^map2gps/$', RedisTestView.as_view(),name='redis_test'),

]
