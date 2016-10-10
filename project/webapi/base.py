#--coding:utf-8--


import os,os.path,sys,struct,time,traceback,signal,threading,datetime


class NotifyMsgType:

	ErrorSystem		= 1000
	ConnectTgsReject = 1001		#认证失效 p1:errcode p2: errmsg

	def toJavaDefs(self):
		pass

def PAGECTRL_RANGE(pgctl,size=20):
	size = pgctl.get('page_size',size)
	num = pgctl.get('page_num',0)
	size = int(size)
	num = int(size)
	return size*num,size*num + size



def USER_ID1(ctx):
	'''
		获取一次消息携带的用户身份编号
	'''
	s = ctx.msg.extra.getValue('__user_id__')
	ids = s.split('#')
	userid = ids[0]
	return int(userid)

def USER_ID2(ctx):
	s = ctx.msg.extra.getValue('__user_id__')
	ids = s.split('#')
	userid = ids[0]
	device_id=None
	if len(ids) >1:
		device_id = ids[1]
	return (int(userid),device_id)

def USER_ID(ctx):
	s = ctx.msg.extra.getValue('__user_id__')
	return int(s)


def ID1(s):
	ids = s.split('#')
	userid = ids[0]
	return int(userid)

def ID2(s):
	ids = s.split('#')
	userid = ids[0]
	device_id=None
	if len(ids) >1:
		device_id = ids[1]
	return (int(userid),device_id)



def MakeUserId(userid,device_id):
	return "%s#%s"%(userid,device_id)


def CALL_USER_ID(userid):
	'''
		构造包含用户编号的附加属性
	'''
	return {'__user_id__':str(userid) }

def CallReturn_Error(errno=0,msg=''):
	import service.lemon_impl
	return service.lemon_impl.CallReturn_t(service.lemon_impl.Error_t(code=errno,msg=msg))

def CallReturn(errno=0,msg='',value=''):
	import service.lemon_impl
	if errno:
		return service.lemon_impl.CallReturn_t(service.lemon_impl.Error_t(False,errno,msg),value)
	return service.lemon_impl.CallReturn_t(service.lemon_impl.Error_t(True),value)

def IntValOfBoolean(val):
	if val :
		return 1
	return 0


def _help_generate_javascript():
	"""
		生成java使用的数据类型
	"""
	f = open('notifytypes.js','w')
	f.write('NotificationType = function(){};\n\n')
	for item in dir(NotifyMsgType):
		if item.find('__')!=-1:
			continue
		val =  getattr(NotifyMsgType,item)
		if callable(val):
			continue
		f.write('NotificationType.%s = %s;\n'%(item,val))
		f.flush()


if __name__ == '__main__':

	_help_generate_javascript()

