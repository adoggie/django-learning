#coding:utf-8

"""

#启动session
MIDDLEWARE
	django.contrib.sessions.middleware.SessionMiddleware
INSTALLED_APPS
	django.contrib.sessions
"""

"""
指定 session 使用cache 系统
默认使用  default Cache
SESSION_CACHE_ALIAS  设置cache的名称
SESSION_ENGINE
	django.contrib.sessions.backends.cache    挥发性存储，满了或cache重启，数据将丢失 (redis可能除外)
	django.contrib.sessions.backends.cached_db  持久化存储到数据库
	django.contrib.sessions.backends.file  存储到文件
		需配置  SESSION_FILE_PATH  默认: tempfile.gettempdir()
"""


"""
Using cookie-based sessions¶
	django.contrib.sessions.backends.signed_cookies
	SECRET_KEY
	 SESSION_COOKIE_HTTPONLY
"""

"""
#设置session 有效期
	SESSION_COOKIE_AGE
	SESSION_EXPIRE_AT_BROWSER_CLOSE

#访问session
request.session
	get(key, default=None)
	keys()
	pop(key, default=__not_given)

	items()
	setdefault()
	clear()
	flush()
	set_expiry(value)
	get_expiry_age()
	get_expiry_date()
	get_expire_at_browser_close()
	clear_expired()
	cycle_key()


SESSION_CACHE_ALIAS
SESSION_COOKIE_AGE
SESSION_COOKIE_DOMAIN
SESSION_COOKIE_HTTPONLY
SESSION_COOKIE_NAME
SESSION_COOKIE_PATH
SESSION_COOKIE_SECURE
SESSION_ENGINE
SESSION_EXPIRE_AT_BROWSER_CLOSE
SESSION_FILE_PATH
SESSION_SAVE_EVERY_REQUEST
SESSION_SERIALIZER

"""
