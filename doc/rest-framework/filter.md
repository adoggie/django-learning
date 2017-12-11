

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


