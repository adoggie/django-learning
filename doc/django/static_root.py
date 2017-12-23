#coding:utf-8

"""
配置静态资源访问 static (只能DEBUG下运行)

 url(r'^static/(?P<path>.*)$',django.views.static.serve),
 django 1.10 第二个view参数必须是callable或者list，而不能是string了，而且不用再指定 {'document_root':settings.STATIC_ROOT,'show_indexes':True}

settings.py
	STATIC_URL = '/static/'
	STATICFILES_DIRS = [
	    os.path.join(BASE_DIR, "static"),
	]
	STATIC_ROOT 无需设置，django自动到 static_dir中匹配资源文件

如何列出目录:
	用户无法直接通过设置 show_indexs实现显示目录文件了，必须强制修改django代码

	django.views.static.serve()
		def serve(request, path, document_root=None, show_indexes=True):

"""
