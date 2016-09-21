#--coding:utf-8--



import os,os.path,sys,struct,time,traceback,signal,threading,copy,base64,urllib,json


import urllib2
import cookielib

HEADERS= \
"""
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4
Cache-Control:max-age=0
Connection:keep-alive
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
"""

class HttpRequest:
	def __init__(self,name=''):
		self.name = name
		self.cookie = cookielib.CookieJar()
		cookie_file = 'cookie.txt'
		# cookie = cookielib.MozillaCookieJar(cookie_file)
		# self.cookie = cookielib.FileCookieJar(cookie_file)
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor( self.cookie))
		self.headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
		for line in HEADERS.split('\n'):
			if not line.strip(): continue
			k,v = line.split(':')
			self.headers[k] = v

		self.method = 'GET'

	def set_header(self,name,value):
		self.headers[name] = value

	def _get_method(self):
		return self.method

	#HttpResponse:
	# 	getheader() getheaders()
	#	msg,version,status,reason
	def get(self,url,dict_obj={},headers={},method='GET'):
		self.method = method

		data = ''
		if dict_obj:
			data = urllib.urlencode(dict_obj)
		url = url.lstrip('/') + '/?'+data
		hdrs = {}
		if headers:
			hdrs = dict( self.headers.items() + headers.items() )
		req = urllib2.Request(url,headers= hdrs )
		req.get_method = self._get_method
		response = self.opener.open(req)
		return response


	def post(self,url,dict_obj={},headers={},method='POST'):
		self.method = method
		data = ''
		if dict_obj:
			data = urllib.urlencode(dict_obj)
		hdrs = {}
		if headers:
			hdrs = dict( self.headers.items() + headers.items() )
		req = urllib2.Request(url,data,headers= hdrs )
		req.get_method = self._get_method
		response = self.opener.open(req)
		return response

	def put(self,url,dict_obj={},headers={},method='PUT'):
		return self.post(url,dict_obj,headers,method)

	def delete(self,url,dict_obj={},headers={},method='DELETE'):
		return self.post(url,dict_obj,headers,method)


	def post_file(self,url,filename,dict_obj={},headers={}):
		from poster.encode import multipart_encode
		from poster.streaminghttp import register_openers

		self.method = 'POST'
		register_openers()

		data = {'file':open(filename,'rb')}
		if dict_obj:
			data.update( dict_obj )

		datagen, _headers = multipart_encode( data )
		if headers:
			_headers.update( headers )

		request = urllib2.Request(url, datagen, _headers)
		response = urllib2.urlopen(request)
		return response

def test_simple():

	import urllib2
	import cookielib
	cookie = cookielib.LWPCookieJar()
	handler=urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)
	response = opener.open('http://www.jd.com')
	for item in cookie:
		print 'Name = '+item.name
		print 'Value = '+item.value

def test_cookie():
	req = HttpRequest('test1')
	url = 'http://192.168.10.100:8088/'
	url = 'http://www.sina.com.cn'
	resp = req.get(url)
	for c in req.cookie:
		print c.name,c.value

	# print resp.read()

if __name__ == '__main__':
	test_cookie()
	# test_simple()