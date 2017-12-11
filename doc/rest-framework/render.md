
## Render输出方式控制 

```python
  1. 直接url构建时指定 render类型
  url(r'^books-2/',  ListAPIView.as_view(queryset=Book.objects.all(),serializer_class= BookSerialier),name='books',renderer_classes=(JSONRenderer,)),
  
  2. 自定义 GenericView的子类，指定 render 类型
  class BookView( generics.ListAPIView ):
    queryset = Book.objects.all()
    serializer_class = BookSerialier
    renderer_classes = (JSONRenderer,) # 直接指定输出的编码方式

  3. settings.py 设定默认render类型 
    REST_FRAMEWORK = {
      'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
       )
    }
    以上制定了两种输出render类型，通过 format 参数 来指定输出类型
	
```


## 默认的Render

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}
```

指定输出Render，注意必须是  list 类型
**renderer_classes = (JSONRenderer, )**

```
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
```

## 支持更多的Render

```
XML：
	 pip install djangorestframework-xml
	'rest_framework_xml.renderers.XMLRenderer',

JSONP :
	pip install djangorestframework-jsonp
	'rest_framework_jsonp.renderers.JSONPRenderer',

YAML:
	pip install djangorestframework-yaml
	'rest_framework_yaml.renderers.YAMLRenderer',
```
