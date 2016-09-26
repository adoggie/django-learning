#coding:utf-8


"""
url(r'^help/', include('apps.help.urls', namespace='foo', app_name='bar'))
url(r'^help/', include(help_patterns, 'bar', 'foo'),name='basic'),

在模板中可以这样来使用，foo:bar:basic来引用，这样对于url逆向解析就不会出错了，其中，application级别
的命名空间包含instance级别的空间，其实,默认，每个app模块都有一个命名空间，就是app的名字

"""