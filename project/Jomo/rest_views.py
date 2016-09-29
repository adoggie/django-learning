#coding:utf-8

from django.utils.crypto import get_random_string
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User, AnonymousUser
from Jomo.models import Test,PigcmsUserinfo
from rest_framework_xml.renderers import XMLRenderer

class SerializerSimpleList(Serializer):
	pass

	# def to_representation(self, instance):
	# 	return {'index':instance}

class TestListView( ListAPIView ):
	# renderer_classes = (JSONRenderer,)
	serializer_class =  SerializerSimpleList

	def get_queryset(self):
		data = []
		for _ in range(100):
			data.append({'index': _ + 1, 'name': get_random_string(20)})
		return data




class SerializerDBTable(ModelSerializer):

	class Meta:
		model = PigcmsUserinfo
		fields = '__all__'
		# fields = ('we','length')

	"""
	按需定制输出
	def to_representation(self, instance):
		return {
			'wxid':instance.wecha_id,
			'wxname':instance.wechaname,
			'tel':instance.tel
		}
	"""

#自定义分页大小
class MyPagination(PageNumberPagination):
	page_size = 10

class TestDBTableView(ListAPIView):
	queryset = PigcmsUserinfo.objects
	serializer_class =  SerializerDBTable
	renderer_classes = (JSONRenderer,)
	pagination_class = MyPagination
	# authentication_classes = (SessionAuthentication
	def filter_queryset(self, queryset):
		return  queryset.all()[:200]

	def get(self,request,*args,**kwargs):
		"""
		自己重写get() ,以上定义的Name些 xxx_class全部失效，完全自己处理数据返回
		自定义的 {status,errcode,errmsg,result} 就在这里自行添加了
		所以基本上从APIView继承就可以了,如果需要分页处理，看看ListViewAPI
		"""
		if  request.user.is_authenticated:
			return Response({'status':0})  #这里直接拒绝掉了
		ser = SerializerDBTable( self.get_queryset(),many=True)
		data = ser.data

		#手动控制分页
		page = PageNumberPagination()
		page.paginate_queryset(self.queryset.all()[:200],request)
		return page.get_paginated_response(ser.data)


		return Response({'result':data})
