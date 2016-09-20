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
