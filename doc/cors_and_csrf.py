
"""
csrf 通过服务器生成随机值，通过cookie下发到浏览器，在POST提交数据时携带此随机值到server，保证请求的合法性 。

# html页面的form加入

{ csrf_token }

"""



"""
cors - 跨域访问管理
其主要是对 HEADER，HTTP-METHOD的控制
浏览器在跨域请求时提交 OPTIONS请求到目标server，server返回是否支持 GET/POST/PUT/DELETE/FETCH等操作.
CORS还可以返回客户机http请求header中可以包含哪些字段


"""

""""
pip install djang-cors-headers
"""

MIDDLEWARE_CLASSES = (
	'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
	'GET',
	'POST',
	'PUT',
	'PATCH',
	'DELETE',
	'OPTIONS'
)
CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_HEADERS = (
	'x-requested-with',
	'content-type',
	'accept',
	'origin',
	'authorization',
	'x-csrftoken',
	'if-version',
	'session-token',
	'token'
)


"""
ajax使用django生成的csrf-token

虽然开启了csrf
 'django.middleware.csrf.CsrfViewMiddleware',
 但实际上django的response并没有产生csrftoken返回到前端，
 这会影响前端ajax程序在发送POST,UPDATE,DELETE,PATCH无法发送有效的csrftoken而请求无效.
 {% csrf_token %}通过form field传递的csrftoken另当别论。

 要解决这个问题，请见 django.middle.ware.csrf 的 process_response()处理函数，其检查
  request.META.get("CSRF_COOKIE_USED") 是否设置，未设置则不会返回csrf的cookie

 1. get_token(request) 函数可以生成新的csrftoken的cookie，所以只需要调用一下get_token()即可
 2. 编写新的middleware，从 CsrfViewMiddleware派生， process_response()中调用get_token()即可。

ajax使用csrftoken最简单的方式使用  restframework/js/csrf.js

"""

