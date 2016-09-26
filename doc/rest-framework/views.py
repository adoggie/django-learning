#coding:utf-8

"""

GenericAPIView
	queryset
	serializer_class
	pagination_class

	只有到GenericeAPIView才具有分页功能
	GenericeAPIView基本上不能直接使用，其的目的是为了组装 诸多mixin成为新的crud接口视图类而存在

CreateAPIView(post) - CreateModelMixin (create)
ListAPIView(get) - ListModelMixin (list)
RetrievAPIView(get) - RetrieveModelMixin(retrieve)

以上接口在使用时，用户根据数据操作的行为crud，分别派生即可，并且重载对应的动作:
	create／list/retrieve/destroy/update/partial_update



"""