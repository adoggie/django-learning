
## SimpleRouter
基本使用方法

```python
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register('users',UserViewSet)
urlpatterns = router.urls 
urlpatterns = [ url('users',include(router.urls))]
```
## DefaultRouter
这种Router类似于SimpleRouter，增加了 api root视图，通过访问 view的根url得到ViewSet的所有Api列表
`(but additionally includes a default API root view, that returns a response containing
hyperlinks to all the list views. It also generates routes 
for optional .json style format suffixes)`.



