#coding:utf-8

from django.db import models

from django.contrib.auth.models import User,AnonymousUser
# Create your models here.


class Application(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField( max_length=100 ,null=True)
	ver = models.CharField(max_length=20,null=True)
	description = models.CharField( max_length= 1000,null=True)
	create_date = models.DateField()

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
	headers = models.CharField(max_length=2000,null=True)
	paramters = models.CharField(max_length=2000,null=True)


class DocumentResponse(models.Model):
	doc = models.ForeignKey(ApiDoc,related_name='apidoc_response_set')
	status = models.CharField(max_length=20,default='200')
	headers = models.CharField(max_length=2000,null=True)
	data = models.CharField(max_length=2000,null=True)


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

class ErrorDef(models.Model):
	doc = models.ForeignKey(ApiDoc)
	code = models.CharField(max_length=20,db_index=True,verbose_name=u'错误编码')
	name = models.CharField(max_length=40,db_index=True,verbose_name=u'错误名称')
	message = models.CharField(max_length=200,null=True)
