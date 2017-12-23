#coding:utf-8

	from django.contrib.auth.decorators import permission_required
	from django.contrib.auth.decorators import login_required

	@login_required
	def my_view(request):

	settings.LOGIN_URL
	@login_required(login_url='/accounts/login/')
