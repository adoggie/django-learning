# -- coding:utf-8 --
# key:value  value is list   2011.6.18
import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,threading
from xml.dom.minidom import  parseString as xmlParseString


# 允许 同名多个配置项:
# name=shanghai
# name=begjin
# getValueList('name') >> [shanghai,beijin]
class SimpleConfig:
	def __init__(self):
		self.props={}
		
	def clear(self):
		self.props={}
		
	def load(self,file):
		try:
			f = open(file,'r')
			lines = f.readlines()
			f.close()
			for line in lines:
				line = line.strip()
				if line[:1] =='#': continue
				try:
					key,val = line.split('=')
					key=key.strip()
					val=val.strip()
					if not self.props.has_key(key):
						self.props[key]=[]
					self.props[key].append(val)
				except:pass
		except:
			pass
		
	def getValue(self,key):
		if self.props.has_key(key):
			return self.props[key][0]
		return ''
	
	def getValueList(self,key):
		if self.props.has_key(key):
			return self.props[key] #
		return []


class EndPoint:
	def __init__(self):
		self.id = ''
		self.name = ''
		self.type = ''
		self.host =''
		self.addr = ''
		self.port = ''



def readEndpoints(xmlfile):
	'''
		读取service.xml定义的所有ep配置参数
	'''
	f = open(xmlfile)
	d = f.read()
	f.close()
	doc = xmlParseString(d)
	r = doc.documentElement

	# endpoints
	epdefs = {} #{EP_IDX:ep}

	e = r.getElementsByTagName('EndPoints')

	e2 = e[0].getElementsByTagName('ep')
	epidx = 1
	for e in e2:
		ep = EndPoint()          # 通信端点类
		ep.id = epidx
		ep.name = e.getAttribute('name')
		ep.type = e.getAttribute('type')
		ep.host = e.getAttribute('host')
		ep.addr = e.getAttribute('address')
		ep.port = int(e.getAttribute('port'))
		epidx+=1
		epdefs[ep.name] = ep        # 记录通信端点
	return epdefs


class YamlConfigReader:
	def __init__(self,conf):
		self.props ={}
		self.conf = conf
		self.read_file(conf)

	def read_file(self,conf):
		import yaml
		f = open(conf)
		self.props = yaml.load(f.read())
		f.close()



