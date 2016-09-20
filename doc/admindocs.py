#coding:utf-8

https://docs.djangoproject.com/en/1.10/ref/contrib/admin/admindocs/

需要docutils这个模块的支持.下载地址是: http://docutils.sf.net/



INSTALLED_APPS
	django.contrib.admindocs

(r'^admin/doc/', include('django.contrib.admindocs.urls'))
