
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