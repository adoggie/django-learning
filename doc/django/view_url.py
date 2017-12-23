#coding:utf-8
from django.views.generic.base import TemplateView

TemplateView.as_view(template_name=xx)

"""
FormView
	当view需要输入验证数据时使用

	forms.Field()
		- error_messages={'required':u'转换文本不能为空'}

Template中 {{form.errors}} 返回错误提示，生成这个错误提示的功能类是：
	forms.util.py 的 ErrorList()  Errordict()／ ErrorList() / flatattr() 函数

"""
