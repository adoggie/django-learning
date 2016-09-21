#--coding:utf-8--


import os,os.path,sys,struct,time,traceback,signal,threading,json
import tcelib as tce

import utils
# from  service.lemon_impl import *
import base,basetype

import init_script

etc_path = init_script.ETC_PATH

tgs_proxies ={}

def getTerminalProxyByUserId(cache,user_id):
	'''
		根据终端用户id查找在连接到哪个tgs服务器

		server_eps.conf 记录tqs对应的接收rpc消息的endpoint名称,
		获取ep名称，通过RpcCommunicator.findEndpoints()得到ep
		ep.impl就是对应服务器接收消息的连接
	'''
	global tgs_proxies
	prx = None
	try:
		user_id = int(user_id)
		key =  basetype.CacheEntryFormat.UserWithTGS%(user_id)
		print 'cache.get:',key
		tgs = cache.get(key)
		if  not tgs:
			print 'user proxy not in cache.'
			return None #not online
		# print key ,tgs_proxies
		prx = tgs_proxies.get(tgs)
		if not prx:
			cf = utils.config.SimpleConfig()
			cf.load(etc_path + '/server_eps.conf')
			epname = cf.getValue(tgs)
			ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(epname)
			prx = ITerminalPrx(ep.impl)
			tgs_proxies[tgs] = prx
	except:
		traceback.print_exc()
	finally:
		if not prx:
			print 'user: %s is not online!'%user_id
		return prx



def getUserDeviceList(cache,user_id):
	'''
		获取用户所有的设备编号
	'''
	devids = cache.get(basetype.CacheEntryFormat.UserWithDevice %user_id)
	return devids


