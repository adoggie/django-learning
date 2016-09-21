# -*- coding: UTF-8 -*-

import smtplib,traceback,os,sys,time,os.path,base64
import urllib,urllib2
import redis

class RedisServer:
	def __init__(self,host='127.0.0.1',port=6379):
		self.addr = (host,port)
		self.cache = redis.StrictRedis(host,port)

	def get(self,key):
		return self.cache.get(key)

	def set(self,key,value,expire=None):
		self.cache.set(key,value,expire)

	def delete(self,key):
		self.cache.delete(key)


if __name__ == '__main__':
	res = RedisServer()
