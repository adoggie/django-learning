#coding:utf

from django.core.cache import cache
# from django_redis.client.DefaultClient
# from django_redis.cache.RedisCache

cache.set('name',9090)
print cache.get('name')