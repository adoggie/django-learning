#coding:utf-8

"""
django 可以将 module对象直接序列化为格式文档 (xml,json,yaml)


"""

from django.core import serializers
data = serializers.serialize("xml", SomeModel.objects.all())

XMLSerializer = serializers.get_serializer("xml")
xml_serializer = XMLSerializer()
xml_serializer.serialize(queryset)
data = xml_serializer.getvalue()


#控制输出字段
from django.core import serializers
data = serializers.serialize('xml', SomeModel.objects.all(), fields=('name','size'))

#反序列化

for obj in serializers.deserialize("xml", data):
    do_something_with(obj)


    