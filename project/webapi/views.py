#coding:utf-8

from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet

from webapi.models import Application, Module


class EasyUiPagination(PageNumberPagination):
	# page_size = 10  # 真正的page_size由easyui.paginator传递过来
	page_query_param = 'page'
	page_size_query_param ='rows'

	def get_paginated_response(self,data):
		return Response(
				{'total':self.page.paginator.count,
				 'rows':data
				 })

class ApplicationSerializer(ModelSerializer):
	class Meta:
		model = Application


"""
虽然开启了csrf
 'django.middleware.csrf.CsrfViewMiddleware',
 但实际上django的response并没有产生csrftoken返回到前端，
 这会影响前端ajax程序在发送POST,UPDATE,DELETE,PATCH无法发送有效的csrftoken而请求无效.
 {% csrf_token %}通过form field传递的csrftoken另当别论。

 要解决这个问题，请见 django.middle.ware.csrf 的 process_response()处理函数，其检查
  request.META.get("CSRF_COOKIE_USED") 是否设置，未设置则不会返回csrf的cookie

 1. get_token(request) 函数可以生成新的csrftoken的cookie，所以只需要调用一下get_token()即可
 2. 编写新的middleware，从 CsrfViewMiddleware派生， process_response()中调用get_token()即可。

"""
class ApplicationViewSet(ModelViewSet):
	serializer_class = ApplicationSerializer
	queryset = Application.objects.all()
	pagination_class = EasyUiPagination

	def get_queryset(self):
		get_token(self.request)
		rs = Application.objects.all()
		return rs

class ApiModuleSerializer(ModelSerializer):
	class Meta:
		model = Module

class ModuleViewSet(ModelViewSet):
	serializer_class = ApiModuleSerializer
	pagination_class = EasyUiPagination
	# queryset = Module.objects.all()

	def get_queryset(self):
		return Module.objects.all()




