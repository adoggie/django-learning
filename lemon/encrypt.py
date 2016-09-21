# -- coding:utf-8 --

__author__ = 'scott'


import utils

def encryptUserToken(auth):
	'''
		auth - AuthResult_t

	'''
	d = auth.marshall()
	token = utils.cipher.encryptToken(d)
	return token

def decryptUserToken(token):
	'''
		return :  AuthResult_t
	'''
	import service.lemon_impl
	d = utils.cipher.decryptToken(token)
	auth = service.lemon_impl.AuthResult_t()
	# d = utils.misc.hashobject2(auth)

	succ,code = auth.unmarshall(d)
	# auth = None
	if not succ:
		auth = None
	return auth

def encryptUserPassword(psw):
	enPsw = utils.cipher.encryptPassword(psw)
	return enPsw

def decryptUserPassword(psw):
	dePsw = utils.cipher.decryptPassword(psw)
	return dePsw

def encryptID(id):
	"""
	加密ID,防止仿冒id导致的非法数据操作
	id 可以是STRING，INTEGER类型
	"""
	id= str(id)
	return id

def decryptID(id):

	return id

def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def encryptCertPassword(psw):
	enPsw = utils.cipher.encPassword(psw)
	return enPsw

def decryptCertPassword(psw):
	dePsw = utils.cipher.decPassword(psw)
	return dePsw