#--coding:utf-8--


import os,os.path,sys,struct,time,traceback,signal,threading,datetime


class ErrorDefs:
	SUCC = (0,'')
	SessionExpired		= 	(1001,u'未登录或会话过期')
	InternalException 	= 	(1002,u'内部异常')
	PasswdIncorret 		=	(2001,u'密码错误')
	UserNameDuplicated  =	(2002,u'登录名重复')
	UserNameNotExisted  =	(2003,u'用户或密码错误')
	SignCodeIncorret    =   (2004,u'验证码错误')
	PermissionDenied	=	(3004,u'权限禁止')
	ParameterIllegal	= 	(3005,u'参数非法')
	UnAuthorizedAccess	= 	(3006,u'请求未授权')
	ObjectNotExisted	= 	(3007,u'对象不存在')
	AccountExisted		= 	(3008,u'帐号名称已存在')
	CertNotExisted      =   (4001,u'无可用证书')
	CertHasUsed         =   (4002,u'导入证书已使用')
	CertNumError        =   (4003,u'导入证书证书数量错误')
	certNameError       =   (4004,u'导入证书证书名错误，请确保证书名相同')
	CertIsNull          =   (4005,u'证书不存在')
	CanNotImportCert    =   (4006,u'服务端用户不允许导入证书')
	CanNotChangeCert	=   (4007,u'可用证书不能手动更改状态')
	SetLicNumError		=   (4008,u'授权终端数量不能小于已用授权终端数')
	SetLicNumBError	    = 	(4009,u'授权终端数量不能大于可授权终端数')
	ExtError			=   (4010,u'导入证书文件中有错误格式')
	ExtNumError			=   (4011,u'cer和p12格式文件数量必须相同')
	AppExisted		    = 	(5001,u'应用标识已存在')
	AppNoLic			= 	(5002,u'所选应用已无可用授权数')
	NoAppAllot			= 	(5003,u'无应用可以匹配')

def generateErrorTypesToJavascript():
	"""
	为javascript开发 转换错误类型
	"""
	jsfile = 'ErrorDefs.js'
	f = open(jsfile,'w')

	pass


