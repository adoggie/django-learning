from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

__author__ = 'zhangbin'

class EasyUiPagination(PageNumberPagination):
	# page_size = 10  # 真正的page_size由easyui.paginator传递过来
	page_query_param = 'page'

	page_size_query_param ='rows'

	def get_paginated_response(self,data):
		return Response(
				{'total':self.page.paginator.count,
				 'rows':data
				 })