#coding:utf-8


django中的slug其实就是表示一个合法的url的一个部分


{{ var }}  定义变量
{% .. %}  调用函数或者语法执行

内建函数
	url 'name' v1 v2  将v1,v2 填充到指定的url路径


"""
＃template page 中显示field 信息

{{ field.label_tag }}: {{ field }}
{{ form.qq.label_tag }}#表示在form 里面定义这个字段的名称
{{ form.qq }}#根据这个字段在form定义的类型来决定。假设是char类型。那就是文本框
{{ form.qq.errors.as_text  }}表示如果表单字段验证失败的话，这个代表错误信息
{{ form.qq.help_text }}如果你在form里定义了这个字段的帮助信息的话，就会在这里显示了
{{ form.qq.value }} 显示 field的值
	- BoundField
"""
