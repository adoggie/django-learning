#coding:utf-8


"""

默认的Render

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}

指定输出Render，注意必须是  list 类型
renderer_classes = (JSONRenderer, )

@api_view(['GET'])
@renderer_classes((JSONRenderer,))

支持更过的Render

XML：
	 pip install djangorestframework-xml
	'rest_framework_xml.renderers.XMLRenderer',

JSONP :
	pip install djangorestframework-jsonp
	'rest_framework_jsonp.renderers.JSONPRenderer',

YAML:
	pip install djangorestframework-yaml
	'rest_framework_yaml.renderers.YAMLRenderer',
"""