#coding:utf-8

"""
archive.py
	extract(path, to_path='')  Unpack the tar or zip file at the specified path to the directory

crypto.py
	get_random_string(length,allows)
	salted_hmac(key_salt, value, secret=None)

duration.py
	duration_string(duration)  计算时长

html.py
	escape()  html 关键字符 文本转义
	escapejs()
	linebreaks()  转义文本为html，自动将换行符替换 为 <br>
	strip_tags()  删除文本中所有 html tag
	strip_spaces_between_tags()
	smart_urlquote()  将url转换成可传递的文本
	urlize()   Converts any URLs in text into clickable links.

http.py
	urlquote()   转换url为可传递的文本
	urlunquote()
	urlencode()
	cookie_date(seconds)  生成cookie 描述字符串
	cookie_date(seconds)  生成cookie 描述字符串
	http_date(epoch_seconds=None) 生成http的时间
	parse_http_date
	urlsafe_base64_encode
	urlsafe_base64_decode
	is_same_domain

numberformat.py
	format(number,...)   格式化数字 ，千万百万...

text.py
	wrap(text,width)   文本隔断
	get_valid_filename  活着一个规则的文件名
			get_valid_filename("john's portrait in 2004.jpg")
    		'johns_portrait_in_2004.jpg'
	compress_string  压缩文本
	compress_sequence
	smart_split(text)
	slugify  删除非 [a-Z0-9],_,-  并转换为小写
	camel_case_to_spaces


"""