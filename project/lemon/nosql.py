#--coding:utf-8--


import os,os.path,sys,struct,time,traceback,signal,threading,json
import datetime
import  utils
# import tcelib as tce
# from  libs.python.sns.showbox import *
import base
# import utils

from pymongo import MongoClient
from bson.objectid import ObjectId

database = None


def hashobject(obj):
	attrs = [s for  s in dir(obj) if not s.startswith('__') and s!='NAME' and s!='_id' ]
	kvs={}
	for k in attrs:
		attr = getattr(obj, k)
		if not callable(attr):
			kvs[k] = attr

	#kvs = {k:getattr(obj, k) for k in attrs}
	return kvs

def get_collection(cls):
	coll = database[cls.NAME]
	return coll

class BaseType:
	def __init__(self,coll):
		self._id = None
		self.coll_name = coll

	def id(self):
		return self._id

	def getId(self):
		return self.id()

	def save(self):
		d = hashobject(self)
		coll = database[self.coll_name]
		if not self._id:
			_id = coll.insert(d)
			self._id = str(_id)
		else:
			coll.update({'_id':ObjectId(self._id)},d)

	@staticmethod
	def collection(coll_name):
		coll = database[coll_name]
		return coll

class Notification(BaseType):
	NAME = 'notification'
	def __init__(self,sender_id=0,target_id=0,type=0,sender_type=0,skipconfirm=False):
		BaseType.__init__(self,Notification.NAME)
		self.sender_id = sender_id
		self.sender_type = sender_type
		self.target_id = target_id
		self.type = type
		self.p1 = None
		self.p2 = None
		self.p3 = None
		self.p4 = None
		self.issue_time = utils.misc.currentTimestamp64()
		self.confirm_time = None
		# self.skipconfirm = skipconfirm

	def assign(self,r):
		obj = self
		obj.sender_id = r['sender_id']               #发送者编号
		obj.sender_type = r['sender_type']               #邀请接者编号
		obj.target_id = r['target_id']             #目标地址（邮件或者短信）,send_type非0时有效
		obj.type = r['type']                #邀请文本消息
		obj.p1 = r['p1']                 #发送方式 0 - 系统内部邀请； 1 - 短信邀请； 2 - 邮件邀请
		obj.p2 = r['p2']             #发送者名称
		obj.p3 = r['p3']              #邀请发起时间
		obj.p4 = r['p4']                #邀请回复时间
		obj.issue_time = r['issue_time']            #接受或者拒绝 0-no_ack ; 1 - accept; 2- reject
		obj.confirm_time = r['confirm_time']

		obj._id = str(r.get('_id'))
		return self

	@classmethod
	def collection(cls):
		return get_collection(cls.NAME)

	@classmethod
	def get(cls,_id):
		coll = BaseType.collection(cls.NAME)
		obj = None
		try:
			r = coll.find_one({'_id':ObjectId(_id)})
			if r:
				obj = cls()
				obj.assign(r)
				obj._id = _id
		except:
			obj = None
			traceback.print_exc()
		return obj

	def toMessage(self):
		import utils
		nm = NotifyMessage_t()
		nm.seq = self.id()
		nm.issuer = self.sender_id	#.splite('#')[0]
		nm.issuer_type = self.sender_type
		nm.type_ = self.type
		nm.issue_time = self.issue_time # utils.misc.maketimestamp64(self.issue_time)
		nm.p1 = self.p1
		nm.p2 = self.p2
		nm.p3 = self.p3
		nm.p4 = self.p4
		# nm.skipconfirm = self.skipconfirm
		return nm


	def toJson(self):
		import json
		d = hashobject(self)
		s =  json.dumps(d)
		return s





class SendMessage(BaseType):
	NAME = 'send_message'
	def __init__(self):
		BaseType.__init__(self,SendMessage.NAME)
		self.sender_id = None               #发送者编号
		self.target_id = None           	#接者编号
		self.team_id = None             	#发送到组的消息则要记录组的编号
		self.issue_time = utils.misc.currentTimestamp64()          #邀请发起时间
		self.confirm_time = None                #确认时间
		self.confirm_result = base.SendMsgStatus.UNACKED            	#0-未确认;  1 -发送已确认
		self.level = None               			#消息级别 1 – 不可丢弃; 2 – 可丢弃
		self.type = None                           #消息类型
		self.content = None                          #文本消息
		self.entities = 0            			#消息包含entites的标志 mask
		self.userdata = None

	def assign(self,r):
		obj = self
		obj.sender_id = r['sender_id']               #发送者编号
		obj.target_id = r['target_id']               #邀请接者编号
		obj.team_id = r['team_id']             #目标地址（邮件或者短信）,send_type非0时有效
		obj.issue_time = r['issue_time']                #邀请文本消息
		obj.confirm_time = r['confirm_time']                 #发送方式 0 - 系统内部邀请； 1 - 短信邀请； 2 - 邮件邀请
		obj.confirm_result = r['confirm_result']             #发送者名称
		obj.level = r['level']              #邀请发起时间
		obj.type = r['type']                #邀请回复时间
		obj.content = r['content']            #接受或者拒绝 0-no_ack ; 1 - accept; 2- reject
		obj.entities = r['entities']
		obj.userdata = r['userdata']
		obj._id = str(r.get('_id'))
		return self

	@classmethod
	def get(cls,_id):
		coll = BaseType.collection(cls.NAME)
		obj = None
		try:
			r = coll.find_one({'_id':ObjectId(_id)})
			if not r:
				obj = cls()
				obj.assign(r)
				obj._id = _id
		except:
			obj = None
			traceback.print_exc()
		return obj

class ImageEntity(BaseType):
	NAME = 'image_entity'
	def __init__(self):
		BaseType.__init__(self,ImageEntity.NAME)
		self.msg_id =   None
		self.image_type = None
		self.width = None                     #图像宽度
		self.height = None                       #图像宽度
		self.content = None                    # in gridfs
		self.save_time = None
		self.length = 0

	def assign(self,r):
		obj = self
		obj.msg_id = r['msg_id']
		obj.image_type = r['image_type']
		obj.width = r['width']
		obj.height = r['height']
		obj.file_id = r['file_id']
		obj.save_time = r['save_time']
		obj.length = r['length']
		obj._id = str(r.get('_id'))

	@classmethod
	def get(cls,_id):
		coll = BaseType.collection(cls.NAME)
		obj = None
		try:
			r = coll.find_one({'_id':ObjectId(_id)})
			if not r:
				obj = cls()
				obj.assign(r)
				obj._id = _id
		except:
			obj = None
			traceback.print_exc()
		return obj

class AudioEntity(BaseType):
	NAME = 'audio_entity'
	def __init__(self):
		BaseType.__init__(self,AudioEntity.NAME)
		self.msg_id = None
		self.audio_type = None
		self.sample = None                        #
		self.channel = None                        #
		self.duration = None                       #
		self.content = None                   #图像内容base64
		self.save_time = None
		self.length = 0

	def assign(self,r):
		obj = self
		obj.msg_id = r['msg_id']
		obj.audio_type = r['audio_type']
		obj.sample = r['sample']
		obj.channel = r['channel']
		obj.duration = r['duration']
		obj.file_id = r['file_id']
		obj.save_time = r['save_time']
		obj.length = r['length']
		obj._id = str(r.get('_id'))

	@classmethod
	def get(cls,_id):
		coll = BaseType.collection(cls.NAME)
		obj = None
		try:
			r = coll.find_one({'_id':ObjectId(_id)})
			if not r:
				obj = cls()
				obj.assign(r)
				obj._id = _id
		except:
			obj = None
			traceback.print_exc()
		return obj


class FindLostPassword(BaseType):
	NAME = 'find_lost_password'
	def __init__(self):
		BaseType.__init__(self,FindLostPassword.NAME)
		self.email = None
		self.phone = None
		self.issue_time = None                   #
		self.expire_time = None                        #
		self.confirm_time = None                       #
		self.sent_time = None                   #
		self.user_id = None
		self.link = 0

	def assign(self,r):
		obj = self
		obj.email = r['email']
		obj.phone = r['phone']
		obj.issue_time = r['issue_time']
		obj.expire_time = r['expire_time']
		obj.confirm_time = r['confirm_time']
		obj.sent_time = r['sent_time']
		obj.user_id = r['user_id']
		obj.link = r['link']
		obj._id = str(r.get('_id'))

	@classmethod
	def get(cls,_id):
		coll = BaseType.collection(cls.NAME)
		obj = None
		try:
			r = coll.find_one({'_id':ObjectId(_id)})
			if not r:
				obj = cls()
				obj.assign(r)
				obj._id = _id
		except:
			obj = None
			traceback.print_exc()
		return obj

	@classmethod
	def collection(cls):
		return get_collection(cls.NAME)



#用户位置信息
class UserLocation(BaseType):
	NAME = 'userlocation'
	def __init__(self,sender_id=0,target_id=0,type=0,sender_type=0):
		BaseType.__init__(self,Notification.NAME)
		self.user_id 	= 0
		self.device_id 	= None
		self.lon 		= 0
		self.lat 		= 0
		self.lon_m 		= 0		#地图坐标
		self.lat_m 		= 0		#地图坐标
		self.speed 		= 0
		self.direction 	= 0
		self.time 		= 0
		self.text 		= None

	def assign(self,r):
		obj = self
		obj.user_id 	= r['user_id']               #
		obj.device_id 	= r['device_id']
		obj.lon 		= r['lon']
		obj.lat 		= r['lat']
		obj.lon_m 		= r['lon_m']
		obj.lat_m 		= r['lat_m']
		obj.speed 		= r['speed']
		obj.direction 	= r['direction']
		obj.time 		= r['time']
		obj.text		= r['text']
		obj._id 		= str(r.get('_id'))
		return self

	@classmethod
	def collection(cls):
		return get_collection(cls.NAME)

	@classmethod
	def get(cls,_id):
		coll = BaseType.collection(cls.NAME)
		obj = None
		try:
			r = coll.find_one({'_id':ObjectId(_id)})
			if r:
				obj = cls()
				obj.assign(r)
				obj._id = _id
		except:
			obj = None
			traceback.print_exc()
		return obj

	def toJson(self):
		import json
		d = hashobject(self)
		s =  json.dumps(d)
		return s




if __name__ == '__main__':
	conn = MongoClient()
	database = conn.test

	print Notification.collection()

	# n = Notification()
	# n.save()
	# n.sender_id = 'sssssss'
	# n.save()
	# AudioEntity().save()

	# print n.id()
'''
	coll = nosql.get_collection(nosql.Invitation.NAME)
	r = coll.find_one({'_id':ObjectId(seq),'target_id':userid})
'''