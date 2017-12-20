#coding:utf-8

"""

GenericAPIView 子类才具有分页控制功能

默认分页设置
DEFAULT_PAGINATION_CLASS  >>  'rest_framework.pagination.PageNumberPagination'.
'PAGE_SIZE': 100

修改分页设置： 扩展类

	class LargeResultsSetPagination(PageNumberPagination):
	    page_size = 1000
	    page_size_query_param = 'page_size'
	    max_page_size = 10000

指定分页类
pagination_class = LargeResultsSetPagination

1. PageNumberPagination
2. LimitOffsetPagination
3. CursorPagination

#手动控制分页
	page = PageNumberPagination()
	page.paginate_queryset(self.queryset.all()[:200],request)
	return page.get_paginated_response(ser.data)


分页的输出需要自行控制，编写自己的分页类
  {
    status,errcode,errmsg,
    page:{ page_num,page_size,count},
    result:[ .. ]
  }
  
对于ListView的数据返回处理时，如果定义了Paginator 则由Paginator生成Response返回到前端 ，如果未定义，则由Serializer对象进行Render出数据返回到前端

class ListModelMixin(object):
    def list(self, request, *args, **kwargs):
    	...
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)   # serializer已完data输出，并将数据交付给Paginator，最终 由Paginator返回Response
	    
        serializer = self.get_serializer(queryset, many=True) # 这里采用serializer处理data
        return Response(serializer.data)  # Response() 内部调用对应的Render进行最终的数据输出
	
"""
