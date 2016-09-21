# coding:utf-8

import time
import traceback
import datetime
from lemon import errors

__author__ = 'chengchaojie'

import json
from errors import ErrorDefs
from intermediate_result import IntermediateResult
from django.http import HttpResponse


class HttpReturn:

	Success = 0
	Failed = 1
	Ecode_Success = 0

	__Auto_Return = True

	def __init__(self, callback=None, auto_return=False):
		self.status = ErrorDefs.InternalException
		self.errcode = None
		self.errmsg = None
		self.result = None
		self.callback = callback

		self.pgctl = {"total": -1}

		HttpReturn.__Auto_Return = auto_return

	def set_record_total(self, count):
		if isinstance(count, int) and count >= 0:
			self.pgctl["total"] = count

	def append_pgctl(self, key, value):
		if key == "total":
			self.set_record_total(value)

		self.pgctl[key] = value

	def set_auto_return(self, auto=False):
		if isinstance(auto, bool):
			HttpReturn.__Auto_Return = auto

			return self
		else:
			return None

	def return_now(self):

		if self.status is None:
			return None

		if self.callback:
			rval = "%s(%s)" % (self.callback, json.dumps(self.get_response_attr(), default=HttpReturn.datetime2timestamp))
		else:
			rval = json.dumps(self.get_response_attr(), default=HttpReturn.datetime2timestamp)
		print rval
		return HttpResponse(rval, content_type='application/json')

	def success_response(self, result=None):

		self.status = HttpReturn.Success
		self.errcode = HttpReturn.Ecode_Success
		self.result = result

		if HttpReturn.__Auto_Return:
			self.return_now()
		else:
			return self

	def error_response(self, ecode=errors.ErrorDefs.ParameterIllegal, emsg=''):
		self.status = HttpReturn.Failed

		if isinstance(ecode, tuple):
			self.errcode = ecode[0]
			self.errmsg = ecode[1]

		print traceback.format_exc()
		# if self.ecode == errors.ErrorDefs.InternalException[0]\
		# 	or self.ecode == errors.ErrorDefs.ParameterIllegal[0]:
		# 	print traceback.format_exc()

		if HttpReturn.__Auto_Return:
			return self.return_now()
		else:
			return self

	def error_resp(self, ecm=None):
		self.status = HttpReturn.Failed

		if not isinstance(ecm, IntermediateResult):
			ecm = IntermediateResult()
			ecm.success = False
			ecm.error_code = ErrorDefs.ParameterIllegal[0]
			ecm.error_message = ErrorDefs.ParameterIllegal[1]

		self.errcode = ecm.get_error_code()
		self.errmsg = ecm.get_error_message()

		print traceback.format_exc()
		if HttpReturn.__Auto_Return:
			return self.return_now()
		else:
			return self

	def get_response_attr(self):

		attr = {}
		attr.update(self.__dict__)
		del attr["callback"]

		return attr

	@staticmethod
	def datetime2timestamp(obj):
		if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
			return time.mktime(obj.timetuple())

		else:
			raise TypeError('%r is not JSON serializable' % obj)




# 发送（转发）公文：标题 发送（转发）公文：XXX 内容：公文已发出，请查收。
# 重发同发送。
#
# 催办 标题 催办消息：公文“XXX”已下发 内容 公文“XXX”已下发，请速收取并办理
#
# 重打印（转发）申请： 标题 重打印（转发）申请：公文"XXX"有一份重打印（转发）申请