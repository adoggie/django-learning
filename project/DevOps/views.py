#!/bin/env python
#coding:utf-8
from django.core.urlresolvers import reverse
from django.forms.forms import Form
from django import forms
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView
from django.views.generic.list import ListView


tool_app_list=[
	{'name':u'my_ip','comment':u'查询您的互联网IP地址','url':'tool-myip'},
	{'name':u'urlencode','comment':u'url路径解析','url':'tool-urlencode'},
]

def my_ip(request):
	text = """
	<h1>
	your browser's ip is :
	 <p>%s </p>
	</h1>
	"""%request.META.get('REMOTE_ADDR')
	return HttpResponse( text )


class ToolsListView(ListView):
	template_name = "devops/tools_list.html"
	def get_queryset(self):
		return tool_app_list


CHOICE_URLENCODE_TYPES=(
	('encode',u'encode'),
	('decode',u'decode')
)

class UrlEncodeForm(Form):
	opts = forms.ChoiceField(CHOICE_URLENCODE_TYPES)
	text1 = forms.CharField(label=u'Original Text',initial=u'some text..',max_length=2000,
							 widget=forms.Textarea(attrs={'class':'input_text'}),
							 help_text=u'must be set',
							 error_messages={'required':u'转换文本不能为空'}
																   )
	# s_to = forms.CharField(max_length=2000,
	# 					   widget=forms.Textarea(attrs={'class':'input_text'}),
	# 						label=u'Result Text',
	# 					   required=False,
	# 					   )


class UrlEncodeView( FormView):
	template_name = "devops/tools_urlencode.html"
	form_class = UrlEncodeForm
	# success_url = 'tool-urlencode'

	def form_valid(self, form):
		import urllib
		# urllib.quote()
		print 'data:', form.cleaned_data['opts']
		opts = form.cleaned_data['opts']
		if opts == 'encode':
			form.result =  urllib.quote(form.cleaned_data['text1']).strip()
		else:
			form.result = urllib.unquote(form.cleaned_data['text1']).strip()

		# return super(UrlEncodeView,self).form_valid(form)   # 默认跳转到 success_url去了
		return self.render_to_response(self.get_context_data(form=form))  #返回成功提交的数据，默认将清除回复到默认Form的填充值

		#如果要返回页面显示之前提交的数据，需要在 Page中调用 {{ form.cleaned_data.s_to }}

	def get_success_url(self):
		return reverse('tool-urlencode')
