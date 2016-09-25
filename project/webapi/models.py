#coding:utf-8

from django.db import models

from django.contrib.auth.models import User,AnonymousUser
# Create your models here.


class Application(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField( max_length=100 ,null=True)
	ver = models.CharField(max_length=20,null=True)
	description = models.CharField( max_length= 1000,null=True)

class Module(models.Model):
	app = models.ForeignKey(Application)
	name = models.CharField( max_length=100 ,null=True)
	description = models.CharField( max_length= 1000,null=True)

class ApiDoc(models.Model):
	"""

	"""
	class Meta:
		unique_together = ()

	REQUEST = 1
	RESPONSE = 2

	GET = 'get'
	POST = 'post'
	PUT = 'put'
	DELETE = 'delete'

	CHOICE_METHOD =(
		(GET,GET),
		(POST,POST),
		(PUT,PUT),
		(DELETE,DELETE)
	)

	module = models.ForeignKey(Module)
	ver = models.CharField(max_length=20,null=True)
	name = models.CharField( max_length=100 ,db_index=True)
	description = models.CharField( max_length= 1000,null=True)
	url = models.CharField(max_length= 200)
	method = models.CharField(max_length=20,default=GET,choices=CHOICE_METHOD)
	comment = models.TextField(null=True)

UTF8 = 'utf-8'
CHOICE_CHAR_ENCODING =(
	(UTF8,UTF8),
)

CONTENT_TYPE_X_FORM = 'x-www-form-urlencoded'
CONTENT_TYPE_JSON = 'json'
CONTENT_TYPE_XML = 'xml'
CONTENT_TYPE_YAML = 'yaml'

CHOICE_CONTENT_TYPE=(
	(CONTENT_TYPE_X_FORM,CONTENT_TYPE_X_FORM),
	(CONTENT_TYPE_JSON,CONTENT_TYPE_JSON),
	(CONTENT_TYPE_XML,CONTENT_TYPE_XML),
	(CONTENT_TYPE_YAML,CONTENT_TYPE_YAML)
)


class Body(models.Model):
	doc =  models.ForeignKey(ApiDoc)
	type = models.IntegerField(default= ApiDoc.REQUEST)
	char_encoding = models.CharField(max_length=40,choices=CHOICE_CHAR_ENCODING,default=UTF8)
	content_type = models.CharField(max_length=60,choices=CHOICE_CONTENT_TYPE,default=CONTENT_TYPE_X_FORM)
	header = models.ForeignKey(ParamerSet)
	data = models.ForeignKey(ParamerSet)

class ParamerSet(models.Model):
	name = models.CharField(max_length=40,db_index=True)

class Parameter(models.Model):
	"""
	支持嵌套
	"""
	INT = 'int'
	STRING = 'string'
	BOOL = 'bool'
	CHOICE_VALUE_TYPE=(
		(INT,INT),
		(STRING,STRING),
		(BOOL,BOOL)
	)
	owner = models.ForeignKey(ParamerSet,related_name='parameter_set')
	name = models.CharField(max_length=40)
	description = models.CharField(max_length=200,null=True)
	value_type = models.CharField(max_length=40,choices=CHOICE_VALUE_TYPE,default=STRING)
	optional = models.BooleanField()                            #是否可选
	default_value = models.CharField(max_length=100,null=True)

	path_depth = models.IntegerField(default=1,db_index=True)   #当前节点相对于root的深度
	path_id = models.CharField(max_length=400,db_index=True)   # node_node2_node3


class ErrorDef(models.Model):
	doc = models.ForeignKey(ApiDoc)
	code = models.CharField(max_length=20,db_index=True,verbose_name=u'错误编码')
	message = models.CharField(max_length=200,null=True)
