
https://docs.djangoproject.com/en/1.10/releases/
https://www.djangoproject.com/download/
  

backwards-incompatible-1-7

django 1.7 必须手动添加 .setup() ,否则出现"AppRegisterNotReady" 的错误
=========
 >>> import django
 >>> django.setup()
  Otherwise, you will hit an AppRegistryNotReady exception.
