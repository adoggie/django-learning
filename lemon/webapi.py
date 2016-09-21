#--coding:utf-8--


import sys,os,os.path,time,struct,traceback,threading,datetime,calendar,string
from xml.dom import getDOMImplementation
import sqlite3
import string,hashlib
import json
#
from django.http import *
from django.shortcuts import render_to_response

import base,errors

TEST = 1
#

class WebCallReturn:
	SUCC = 0
	FAILED = 1
	def __init__(self,status = FAILED,
	             ecode= errors.ErrorDefs.InternalException,emsg=''):
		self.status = status
		self.ecode = ecode
		self.emsg = emsg
		self.result ={}
		self.kvs={}
		self.callback = None

	def setCallBackJsonp(self,callback):
		self.callback = callback
		return self

	def assign(self,result):
		'''
			赋值返回值
		'''
		self.result = result
		return self

	def setValue(self,key,value):
		self.kvs[key] = value

	def setPageCtrlValue(self,prop,value):
		key = self.kvs.get('pgctl')
		if not key:
			self.kvs['pgctl'] ={}
		self.kvs['pgctl'][prop] = value

	def _httpResponse(self):
		'''
			if jsonp:
				callback_funcName = GET.get('callback')

		'''
		self.kvs['status'] = self.status
		self.kvs['errcode'] = self.ecode
		if self.emsg:
			self.kvs['errmsg'] = self.emsg
		if self.result:
			self.kvs['result'] = self.result
		return json.dumps(self.kvs)

	def httpResponse(self):
		'''
		for Django http-return

		'''
		from django.conf import settings

		self.kvs['status'] = self.status
		self.kvs['errcode'] = self.ecode
		if self.emsg:
			self.kvs['errmsg'] = self.emsg
		if self.result is not None:
			self.kvs['result'] = self.result
		# if TEST:
		# 	return self.kvs
		# else:
		rval = json.dumps(self.kvs)
		if self.callback:
			rval = '%s(%s)'%(self.callback,rval)
		if settings.DEBUG:
			print rval
		return HttpResponse(rval,content_type='application/json')

	def httpResponse2(self):
		return self._httpResponse()

	def __str__(self):
		return self.httpResponse2()

def SuccCallReturn():
	return WebCallReturn(status=WebCallReturn.SUCC,ecode=0)

def FailCallReturn(ecode=errors.ErrorDefs.InternalException,emsg=''):
	if isinstance(ecode,tuple):
		ecode,emsg = ecode
	if not emsg and ecode == errors.ErrorDefs.InternalException:
		print traceback.format_exc()
	return WebCallReturn(ecode=ecode,emsg=emsg)


def exception_catch(func):
	def entering(*args,**kw):
		try:
			return func(*args,**kw)
		except:
			return WebCallReturn( emsg = traceback.format_exc()).httpResponse()

	def exiting():
		pass
	return entering

def webapi_call(func):
	def entering(*args,**kw):
		try:
			r = args[0]
			cb = GET(r,'callback')
			result = func(*args,**kw)
			if not cb or TEST:
				return result.httpResponse2()
			d = '%s(%s)'%(cb,json.dumps(json.dumps(result.kvs)))
			return HttpResponse(d,mimetype='application/json')

		except:
			return FailCallReturn(emsg = traceback.format_exc()).httpResponse2()

	def exiting():
		pass
	return entering


def GET(r,name,default=None,post = False):
	val = r.POST.get(name)
	if not val:
		val = r.GET.get(name)
		if not val:
			val = default
	return val

def HEADER(r,name,default=None):
	val = r.META.get('HTTP_'+ name.upper() )
	if not val:
		val = default
	return val

def sessionValue(r,name,default=None):
	# if name == 'user_id':
	# 	return 2
	# if name == 'user_role':
	# 	return 3

	val = r.session.get(name)
	if not val:
		val = default
	return val

QUERY_PAGESIZE = 100

def getDataPagingParams(r):
	query_parameters = GET(r, "query_parameters")
	if query_parameters:
		query_parameters = json.loads(query_parameters)
		pgctl = query_parameters.get("pgctl")
	else:
		pgctl = GET(r,'pgctl')
	start = 0
	size = 10000000
	if pgctl:
		try:
			if not query_parameters:
				pgctl = json.loads(pgctl)
			start = int( pgctl.get('page_num',0) )
			size = int( pgctl.get('page_size',QUERY_PAGESIZE))
			if start:
				start -= 1
		except:
			pass
	print 'paging:',start*size,start*size+size
	return start*size,start*size+size