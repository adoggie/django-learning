#coding:utf-8

"""

django1.10 版本与诸多第三方组件不兼容  请考虑1.9.10，兼容老款MiddleWare

	django-cors-headers  X

	为了支持 旧版的 MiddleWare，引入了 MIDDLEWARE_CLASSSES (settings.py )
	要求将 第三方的 middleware放入MIDDLEWARE_CLASSES即可

	https://docs.djangoproject.com/en/1.10/releases/1.10/#new-style-middleware

"""