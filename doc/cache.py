#coding:utf-8


#settings.py

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]


#默认的缓存
{
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
	    'LOCATION': 'unique-snowflake',
    }
}

"""
Django的缓存系统的开源项目：https://github.com/niwibe/django-redis

"""

'django.core.cache.backends.db.DatabaseCache'
'django.core.cache.backends.dummy.DummyCache'
'django.core.cache.backends.filebased.FileBasedCache'
'django.core.cache.backends.locmem.LocMemCache'
'django.core.cache.backends.memcached.MemcachedCache'
'django.core.cache.backends.memcached.PyLibMCCache'


#伪缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}



# python manage.py createcachetable

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table_name',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 2000
        }
    }
}

# memcahced 缓存支持
# https://pypi.python.org/pypi/python-memcached

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [ '127.0.0.1:11211', '172.19.26.242:11211',]  #多memcached server 配置
    }
}



#缓存页面
from django.views.decorators.cache import cache_page
@cache_page(60 * 15)
# 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性

#在url中指定缓存
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^foo/([0-9]{1,2})/$', cache_page(60 * 15)(my_view)),
]


"""
直接访问缓存
如果连接了redis,memcache之类的直接当第三方cache来使用 (简单配置好settings.py 的 CACHE)
"""

from django.core.cache import caches
cache1 = caches['myalias']  #获取后端配置的cache

from django.core.cache import cache # equivalent to caches['default'].

# cache methods:

.set(key, value, timeout)
.get(key)
.get_or_set('my_new_key', 'my new value', 100)
.get_many(['a', 'b', 'c'])
.set_many({'a': 1, 'b': 2, 'c': 3})
.delete('a')
.delete_many(['a', 'b', 'c'])
.clear()
.incr('num')
.incr('num', 10)
.decr('num')
.decr('num', 5)
.close()

#  KEY_PREFIX   设置key的前缀 (settings.py)



