

from django.contrib.auth.forms import AdminPasswordChangeForm


"""

Form(BaseForm)

html输出:
	as_table/as_ul/as_p

构造参数 :
  data - 一般是 request.POST

	Form.clean()  成功需要返回 校验ok的数据集合，必须格式类同self.cleaned_data
	Form.is_valid() 验证数据是否合法 ,调用时 内部调用full_clean() 来生成 errors
	Form.errors		可通过form.add_error()添加错误
	Form.errors.as_data()
	Form.errors.as_json(escape_html=False)
	Form.add_error(field, error)

	Form.cleaned_data  合规的数据

	Form.is_bound  如果构造参数 data != None 则True
		  self.is_bound = data is not None or files is not None

	BaseForm._clean_fields()  会根据Form中定义的字段挨个查找  clean_xxxx()函数，并返回到 cleaned_data

	Form.full_clean()  由 is_valid() 调用触发，并进行field的数据验证 "_clean_fields() "
		full_clean() 先进行 各个field的验证，并且调用自定义的 clean_xxx()验证，这些验证都将结果写入cleaned_data,
				然后调用clean()方法，如果用户重写了clean(),那需要往cleaned_data中添加修改数据，并返回 cleaned_data
				最后调用  _post_clean()  这个一般不对用户开放
PS:
	self.data = data or {} 这个语法比较好
"""



"""
ModelForm 用户可以重写的函数 :
	clean(self) 	-  返回新的 cleaned_data
	clean_xxxx(self)  -  自定义xxx字段的验证，在这里可以对提交数据格式的转换成Model要求的格式，如果数据错误无法转换 抛出
				ValidationError 异常，结果就不会加入 cleaned_data
	save(self,commit=True) - 存在的更新，不存在的记录创建,对于Model中不存在的字段，可以重载save()进行字段的配置和赋值

examples:

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)					# 错误就抛出异常 ，否则返回验证过的字段数据
		return password2

"""

"""
ModelForm 构造参数：
	data - request.POST
	initial -
	instance - 数据库表记录对象 ，非空表示数据更新

#ModelForm依赖定义数据表对象

Meta:
	model = xxx
	fields = (xx,..)


#自定义Form 校验 clean()

	from django import forms
	class ContactForm(forms.Form):

		def clean(self):
			cleaned_data = super(ContactForm, self).clean()
			cc_myself = cleaned_data.get("cc_myself")
			subject = cleaned_data.get("subject")

			if cc_myself and subject and "help" not in subject:
				msg = "Must put 'help' in subject when cc'ing yourself."
				self.add_error('cc_myself', msg)
			return cleaned_data

"""