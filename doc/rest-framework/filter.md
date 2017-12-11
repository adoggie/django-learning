

## Filter 

filter用于查询参数自动化过滤，省去自定义查询过滤的代码

不使用过滤器的查询一般这么做：
```python

class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    def get_queryset(self):
        queryset = Purchase.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset
        
```

## 第三方filter

### django-filter 

```bash 
pip install django-filter
```

```python
settings.py 配置 

INSTALLED_APPS = [
    ...
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
```

采用过滤器使工作更简单
```
from django_filters.rest_framework import DjangoFilterBackend

class UserListView(generics.ListAPIView):
    ...
    filter_backends = (DjangoFilterBackend,) 指定查询过滤器
    filter_fields = ('category', 'in_stock') 限定查询条件参数
```


## 关于 filter_set 
django-filter
[https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html](https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html)


## SearchFilter 

搜索过滤的参数是 `search` 

```
filter_backends = (SearchFilter,)
search_fields = ('username', 'email')  指定搜索字段

http://example.com/api/users?search=russel
以上请求 将在 username,email字段中检索 russel 为内容的匹配项 。  

```
如果设置了  search_fields 则 SearchFilter起效 , 以下是控制过滤内容的语法规则 ： 
```
   
    The search behavior may be restricted by prepending various characters to the search_fields.

    '^' Starts-with search.
    '=' Exact matches.
    '@' Full-text search. (Currently only supported Django's MySQL backend.)
    '$' Regex search.

```
    



