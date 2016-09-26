#conding:utf-8


rest_framwork/utils/formatting.py
	dedent()  删除文本前导空格字符
	camelcase_to_spaces()  转换驼峰单词为 空格相间的单词
		" Translate 'CamelCaseNames' to 'Camel Case Names'. "

humanize_datetime.py
	datetime_formats()   格式化 'YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]'
	date_formats() 	'YYYY[-MM[-DD]]'
	time_formats()  'hh:mm[:ss[.uuuuuu]]'

urls.py
	replace_query_param(url, key, val)  替换url中的参数
	remove_query_param(url, key)		删除url中的参数