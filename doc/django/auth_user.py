#coding:utf-8

'''
扩展 auth.models.User 的方法：
1. Proxy 模式
2. Profile 模式
	采用OneToOne来扩展非认证相关的用户信息
'''
	from django.contrib.auth.models import User
	class Employee(models.Model):
	    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User删除时级联删除Employee


#权限Permission

	user.has_perm('myapp.change_bar')
    permission = Permission.objects.get(codename='change_bar')
    user.user_permissions.add(permission)


#AnonymousUser
	当用户未登录，django自动创建 此类型用户对象 request.user
	使用  is_authenticated 判断用户是否登录


#用户登录处理:
	user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)

    from django.contrib.auth import logout
    logout(request)

#未登录跳转
	if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

#登录限定
	@login_required
	settings.LOGIN_URL

#通过 auth.views 直接跳转到 settings.LOGIN_URL

	from django.contrib.auth import views as auth_views
	url(r'^accounts/login/$', auth_views.login),

#基于类的View的登录限定
	LoginRequiredMixin
	from django.contrib.auth.mixins import LoginRequiredMixin
	class MyView(LoginRequiredMixin, View):
	    login_url = '/login/'
	    redirect_field_name = 'redirect_to'


#使用auth自带的授权操作view
	django.contrib.auth.urls

	urlpatterns = [
        url('^', include('django.contrib.auth.urls')),
	]
	会引入auth包内一下view

	^login/$ [name='login']
	^logout/$ [name='logout']
	^password_change/$ [name='password_change']
	^password_change/done/$ [name='password_change_done']
	^password_reset/$ [name='password_reset']
	^password_reset/done/$ [name='password_reset_done']
	^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
	^reset/done/$ [name='password_reset_complete']


	更改显示模板
	urlpatterns = [
	    url(
	        '^change-password/$',auth_views.password_change,{'template_name': 'change-password.html'}
	    ),
	]
