#--coding:utf-8--


import os,os.path,sys,struct,time,traceback,signal,threading,datetime


# import tcelib as tce


class ErrorDefs:
	SUCC = 0
	Undefined = 0xffff

	UserTokenInvalid	= 1000
	InternalException 	= 	1001

	PasswdIncorret 		=	1002
	UserNameDuplicated  =	1003

	TextTooShort 		= 	1004
	TextTooLong 		= 	1005
	InvalidFormat_Email = 1020
	InvalidFormat_Phone = 1021
	InvalidFormat_BorthDay = 1022
	InvalidFormat_Digits  = 1023

	DataInsufficient = 1003
	DataBaseError  =2001

	FileNotExisted = 3000
	FileOpenFailed = 3001
	NetworkNotAvaliable = 3002
	HostUnreachable  = 3002



	UserNotExisted =5001
	UserTeamNotExisted = 5002
	NameDuplicated = 5003
	UserNameDuplicated = NameDuplicated
	UserIdNotExisted = 5004
	UserIsFriend = 5005
	UserNameIsNULL=5006
	UserPasswdIsNULL = 5007
	UserEmailInvalid = 5009
	ParametersInvalid = 5020

	InputDataCorrupted = 5008
	EmailDuplicated = 5010
	PasswdLengthError = 5011  # too short or too long
	HaveNotSupported = 9001

	TargetInvalid = 6001
	IllegalOperation = 6002 #违法操作
	TargetObjectNotExisted = TargetInvalid
	UserTokenIllegal = UserTokenInvalid     #用户令牌错误
	DeviceIdNotMatchedInUserToken = 6003	#登陆时传递的设备编号与token不一致
	UserTokenSessionExpired = 6004 			# Token 过期
	UserAnotherPlaceLogin = 6005
	DataDuplicated = NameDuplicated



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

