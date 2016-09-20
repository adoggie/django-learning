#coding:utf-8



 INSTALLED_APPS
    django.contrib.auth, \
    django.contrib.contenttypes, \
    django.contrib.messages
    django.contrib.admin

MIDDLEWARE
	django.contrib.auth.middleware.AuthenticationMiddleware
	django.contrib.messages.middleware.MessageMiddleware

TEMPLATES (context_processors)

	django.contrib.auth.context_processors.auth
	django.contrib.messages.context_processors.messages

# manage.py createsuperuser

在urls.py 增加：

from django.contrib import admin
admin.autodiscover()
(r'^admin/(.*)', admin.site.root),

使得 admin 能管理app的model，需在app下手动添加 admin.py

    from django.contrib import admin
    from .models import Article

    admin.site.register(Article)  #注册一个mode到管理界面

为自定义表管理行为需要为每个Model定义 ModelAdmin
	class ArticleAdmin(admin.ModelAdmin):
        list_display = ('title', 'is_published')

    admin.site.register(Article, ArticleAdmin)  # 管理界面能展示两列属性


list_filter = ('company__name',)