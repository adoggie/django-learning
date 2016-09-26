#coding:utf-8

"""
前端js开发时，充分利用 restframework提供的static资源 ,
直接引入 rest_framework/js/csrf.js 即可自动完成 csrf-token的获取 ( server端要开启 crsfMiddleWare)

restframework 自带了js包括:  booststrap,ajax-form ,jquery,prettify(格式化代码)

	deafult.js
		prettyPrint() 高亮输出json代码

	<link rel="stylesheet" type="text/css" href="{% static "rest_framework/css/bootstrap.min.css" %}"/>
    <link rel="stylesheet" type="text/css" href="{% static "rest_framework/css/bootstrap-tweaks.css" %}"/>
	<link rel="stylesheet" type="text/css" href="{% static "rest_framework/css/prettify.css" %}"/>
    <link rel="stylesheet" type="text/css" href="{% static "rest_framework/css/default.css" %}"/>

	{% block script %}
		<script src="{% static "rest_framework/js/jquery-1.11.3.min.js" %}"></script>
		<script src="{% static "rest_framework/js/ajax-form.js" %}"></script>
		<script src="{% static "rest_framework/js/csrf.js" %}"></script>
		<script src="{% static "rest_framework/js/bootstrap.min.js" %}"></script>
		<script src="{% static "rest_framework/js/prettify-min.js" %}"></script>
		<script src="{% static "rest_framework/js/default.js" %}"></script>
		<script>
			$(document).ready(function() {
				$('form').ajaxForm();
			});
		</script>
  	{% endblock %}

"""
