#coding:utf-8

django采用默认的认证方式

AUTHENTICATION_BACKENDS
	[default] django.contrib.auth.backends.ModelBackend

可以自行开发自己的认证后端 ，PermissionDenied 异常抛出表示 authoricate() 失败
	class MyBackend(object):
        def authenticate(self, request, username=None, password=None):
		def get_user(self,user_id)

	get_group_permissions()
	get_all_permissions()
	has_perm()
	has_module_perms())
	以上接口需实现


