#coding-utf-8

"""

Throttling
用户控制api请求的频率

rest如何识别客户端 ：
 	rest通过 http头中的  X-Forwarded-For and Remote-Addr 来区别用户, 前者代表nat内部出来的请求经过的代理服务proxy
 	后者表示nat的ip地址

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}


rest记录api请求频率的次数保存在django的后端cache中 ，rest默认使用django的default cache设置，
	如需修改cache ，则需要扩展Throttle类，并更改使用的cache名称

	class CustomAnonRateThrottle(AnonRateThrottle):
    	cache = get_cache('alternate')


视图类控制
	class ExampleView(APIView):
		throttle_classes = (UserRateThrottle,)


函数级控制
	@api_view(['GET'])
	@throttle_classes([UserRateThrottle])
	def example_view(request, format=None):


AnonRateThrottle
	匿名用户速率控制 ， 速率见 DEFAULT_THROTTLE_RATES[anon]

UserRateThrottle
	登陆用户速率控制

扩展Throttle
	class BurstRateThrottle(UserRateThrottle):
    	scope = 'burst'

	'DEFAULT_THROTTLE_RATES': {
        'burst': '60/min',
        'sustained': '1000/day'
    }


"""