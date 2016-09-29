#!/bin/env python
#coding:utf-8
import cookielib

from django.core.urlresolvers import reverse
from django.forms.forms import Form
from django import forms
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView, DeleteView
from django.views.generic.list import ListView


tool_app_list=[
	{'name':u'my_ip','comment':u'查询您的互联网IP地址','url':'tool-myip'},
	{'name':u'urlencode','comment':u'url路径解析','url':'tool-urlencode'},
	{'name':u'hash CODE','comment':u'哈希编码 MD5,Rainbow-Table,SHA1,SHA256','url':'tool-hash'},
	{'name':u'base64E','comment':u'Base64','url':'tool-base64'},
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





class SimpleInputForm(Form):
	text1 = forms.CharField(label=u'',initial=u'some text..',max_length=2000,
							 widget=forms.Textarea(attrs={'class':'input_text'}),
							 help_text=u'must be set',
							 error_messages={'required':u'转换文本不能为空'})

class SimpleInputProcessView(FormView):
	template_name = "devops/tools_process.html"
	form_class = SimpleInputForm

	def form_valid(self, form):
		return self.render_to_response(self.get_context_data(form=form))  #返回成功提交的数据，默认将清除回复到默认Form的填充值

	# def get_success_url(self):
	# 	return reverse('tool-urlencode')

class UrlEncodeForm(SimpleInputForm):
	CHOICE_URLENCODE_TYPES=(
		('encode',u'encode'),
		('decode',u'decode')
	)
	opts = forms.ChoiceField(CHOICE_URLENCODE_TYPES)

class UrlEncodeView( SimpleInputProcessView):
	form_class = UrlEncodeForm
	success_url = '/t/urlencode'
	def form_valid(self, form):
		import urllib
		print 'data:', form.cleaned_data['opts']
		opts = form.cleaned_data['opts']
		if opts == 'encode':
			form.result =  urllib.quote(form.cleaned_data['text1']).strip()
		else:
			form.result = urllib.unquote(form.cleaned_data['text1']).strip()
		# return super(UrlEncodeView,self).form_valid(form)   # 默认跳转到 success_url去了
		return self.render_to_response(self.get_context_data(form=form))  #返回成功提交的数据，默认将清除回复到默认Form的填充值
		#如果要返回页面显示之前提交的数据，需要在 Page中调用 {{ form.cleaned_data.s_to }}



class Base64Form(SimpleInputForm):
	CHOICE_URLENCODE_TYPES=(
		('encode',u'encode'),
		('decode',u'decode')
	)
	opts = forms.ChoiceField(CHOICE_URLENCODE_TYPES)

class Base64View( SimpleInputProcessView):
	form_class = UrlEncodeForm
	success_url = '/t/base64/'
	def form_valid(self, form):
		import base64

		opts = form.cleaned_data['opts']
		if opts == 'encode':
			form.result =  base64.b64encode(form.cleaned_data['text1']).strip()
		else:
			form.result = base64.b64decode(form.cleaned_data['text1']).strip()
		return super(Base64View,self).form_valid(form)


class Md5EncodeForm(SimpleInputForm):
	CHOICE_ENCODE_TYPES=(
		('md5',u'MD5 calc'),
		('md5-rainbow',u'Rainbow Query'),
		('sha1',u'sha1 calc'),
		('sha256',u'sha256 calc'),
		('uuid',u'UUID gen'),
		('password-12-1',u'password-12-1'),
		('password-12-2',u'password-12-2'),
	)
	CHOICE_ENTRY_NUM=(
		('1','1'),
		('5','5'),
		('15','15'),

	)
	opts = forms.ChoiceField(CHOICE_ENCODE_TYPES)
	num = forms.ChoiceField(CHOICE_ENTRY_NUM,label=u'生成数量')

class Md5EncodeView(SimpleInputProcessView):
	form_class = Md5EncodeForm
	success_url = '/t/hash/'

	def form_valid(self, form):
		import hashlib
		data = form.cleaned_data['text1'].strip()

		result = ''
		ops = form.cleaned_data['opts']

		if ops == 'md5-rainbow':
			return self.rainbow(form)

		for n in range(int(form.cleaned_data['num'])):
			if ops == 'uuid':
				import uuid
				result += uuid.uuid4().hex+'\n'

			if ops =='password-12-1':
				result += self.random_password()+'\n'

			if ops =='password-12-2':
				result += self.random_password2()+'\n'

		if ops in ('md5','sha1','sha256'):
			m = hashlib.md5()
			if ops == 'sha1':
				m = hashlib.sha1()
			if ops =='sha256':
				m = hashlib.sha256()
			m.update(data)
			result = m.hexdigest()

		form.result = result
		return super(Md5EncodeView,self).form_valid(form)

	def random_password(self,size = 12):
		import string,random
		N = size
		return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

	def random_password2(self,size = 12):
		import string,random
		N = size
		return ''.join(random.choice(string.letters + string.digits) for _ in range(N))




	def rainbow(self,form):
		"""fd03058401369729668d1dc2cdcc7525
		curl  --get --include  'http://apis.baidu.com/chazhao/md5decod/md5decod?md5=b035b895aae7ea345897cac146a9eee3369c9ef1'  -H 'apikey:您自己的apikey'
		"""
		import urllib2,urllib,json

		cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor( cookie))

		data = form.cleaned_data['text1'].strip()
		url = 'http://apis.baidu.com/chazhao/md5decod/md5decod?md5=%s'%data
		req = urllib2.Request(url,headers= {'apikey':'fd03058401369729668d1dc2cdcc7525'} )
		result = 'decode Error!'
		try:
			resp = opener.open( req)
			ret = resp.read()
			obj = json.loads( ret )
			print ret

			if obj.get('error',0) !=0:
				result = obj.get('msg')
			else:
				result = obj['data']['md5_src']

		except:
			import traceback
			traceback.print_exc()
		form.result =result
		return super(Md5EncodeView,self).form_valid(form)