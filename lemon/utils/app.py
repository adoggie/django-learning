# -*- coding: UTF-8 -*-

import smtplib,traceback,os,sys,time,os.path,base64
import copy

# from pymongo import MongoClient
# from bson.objectid import ObjectId
# import gridfs

import config


class BaseAppServer:
	def __init__(self,name):
		self.name = name
		self.yamlcfg = None
		self.servicefile = None
		self.conf = None
		self.communicator = None
		self.cache = None
		self.mongo = None
		self.fs = None
		BaseAppServer._handle = self

	def getConfig(self):
		return self.conf

	def preInitialize(self):
		'''
		拾取参数 - name

		'''
		argv = copy.deepcopy(sys.argv)
		try:
			while argv:
				p = argv.pop(0).strip().lower()
				if p =='-name':
					name = argv.pop(0)
					self.name = name
		except:
			traceback.print_exc()

	def init(self,yamfile,servicefile=''):
		self.preInitialize()
		self.yamlcfg = config.YamlConfigReader(yamfile).props
		self.servicefile = servicefile
		self.conf = self.yamlcfg.get(self.name)
		self.initRpc()
		self.initNosql()
		self.initCache()

	def initNosql(self):
		import mongo

		cfg = self.yamlcfg[self.conf['mongodb']]
		self.mongo = mongo.Connection(cfg['database'],host=cfg['host'],port=cfg.get('port',27017))
		self.fs = mongo.Connection('fs',host=cfg['host'],port=cfg.get('port',27017))

	def initCache(self):
		import redis2 as redis
		cfg = self.yamlcfg[self.conf['redis']]
		self.cache = redis.RedisServer(host=cfg['host'])


	def initRpc(self):
		import tcelib as tce
		self.communicator = tce.RpcCommunicator().instance()
		if self.servicefile:
			self.communicator.init(self.name).initMessageRoute(self.servicefile)


	def run(self):
		print 'Service [%s] started..'%self.name

	def getEndPoint(self,name):
		return self.communicator.currentServer().findEndPointByName(name)

	def getEndPointConnection(self,name):
		return self.getEndPoint(name).impl

	def setRpcMQCircuit(self,conn_call,conn_back):
		if isinstance(conn_call,str):
			conn_call = self.getEndPointConnection(conn_call)
		if isinstance(conn_back,str):
			conn_back = self.getEndPointConnection(conn_back)
		conn_call.setLoopbackMQ(conn_back)


	_handle = None
	@classmethod
	def instance(cls):
		if not cls._handle :
			cls._handle = cls()
		return cls._handle


if __name__ == '__main__':
	pass #send_sms("13916624477","老张,新年快乐诶!!!")