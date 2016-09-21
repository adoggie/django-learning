# -*- coding: UTF-8 -*-

import smtplib,traceback,os,sys,time,os.path,base64


from pymongo import MongoClient
from bson.objectid import ObjectId
import gridfs

class Connection:
	def __init__(self,dbname,host='localhost',port=27017):
		self.addr = (host,port)
		self.dbname = dbname
		self.conn = MongoClient(host,port)
		self.db = self.conn[self.dbname]
		self.fs = None

	def getGridFs(self):
		if not self.fs:
			self.fs = gridfs.GridFS(self.db)
		return self.fs

	def new_file(self,filename):
		if not self.fs:
			self.fs = gridfs.GridFS(self.db)
		handle = None
		handle = self.fs.new_file(filename=filename)
		return handle # GridIn

	def put_file(self,content,filename=None):
		'''
			将content整个内容以文件方式存入，返回ObjectId()对象
		'''
		if not self.fs:
			self.fs = gridfs.GridFS(self.db)
		_id = self.put(content,filename = filename )
		return _id

	def remove_file(self,file_id):
		'''
			gridfs 中删除指定的文件存储
		'''
		if isinstance(file_id,str):
			file_id = ObjectId(file_id)
		self.fs.delete(file_id)



def test():
	conn = MongoClient('192.168.10.99')
	db = conn['sns']
	rs = db.notification.find({'target_id':'aa'})
	print dir(rs)
if __name__ == '__main__':
	test()