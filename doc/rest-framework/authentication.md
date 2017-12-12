
## restframework携带三种认证方法:

	BasicAuthentication
	SessionAuthentication
	TokenAuthentication


## 缺省开启的认证方式
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
```

### BasicAuthentication :
```
每一次api请求都携带用户名和密码， 从http头部获取认证信息，包含登陆用户名和口令( base64编码)，到数据库验证用户是否合法，并返回user
"
WWW-Authenticate: Basic realm="api"
"
request.user  将被设置
request.auth  为None
```
### SessionAuthentication：
```
简单的检查request.user是否为空或者是否激活 is_active ,如果已登陆则返回user
	request.user  将被设置
	request.auth  为None
	当restframwework与django页面登陆验证共享时，这是个简单的方法，django页面的登陆结果在rest中直接使用 。
	SesionAuthentication 一般都在浏览器页面的ajax操作的场景 ， rest使用django的用户认证结果，但必须注意 csrf 问题
	为保证安全，每个ajax请求需要携带 crsf token
```

### TokenAuthentication
```
这种认证方式是，为当前存在的用户User创建一个token，并保存在数据库中，以后用户登陆就使用此token作为凭证。

生成token、发布token和管理token是个问题 。

令牌认证方式，每一次webapi请求都会携带一个认证token
使用时必须加入 'rest_framework.authtoken' 到 INSTALLED_APPS 列表 ，并且需要同步数据库，其将创建用户user相关的token表

"Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"

request.user user
request.auth  rest_framework.authtoken.models.Token

```
**设置用户添加时自动生成Token**
捕捉 `User`的post_save 信号
```
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)  #that is 'auth.User'
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

**为已存在用户创建Token** 
```python
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

for user in User.objects.all():
    Token.objects.get_or_create(user=user)
```



## 代码中使用认证方式

```python
class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
```
此view被请求前进行 SessionAuthentication认证，如果把失败则进行用户名＋口令方式认证

```
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def example_view(request, format=None):

```
注意：
配置了认证类之后，request到达，APIView在initial阶段进行身份认证，如果用户未登录，则reqeust.user为Anomymouse用户类型，其并不会返回HTTP错误
所以需要编写MiddleWare在项目中控制 访问Api必须被授权才能访问，拦截掉所有请求，直接返回自定义的错误码信息 { status=0,errcode=xxx }




```
奇怪问题：
  django 的auth完成用户登录，request.user设置为 User对象
  但在随后DRF接口调用时，drf的request.user是AnonymousUser对象，查看rest_framework.views.Request代码，将__init__()的
   "self.authenticators = authenticators or ()" 注释掉，居然就好了，request.user就是之前login的User对象了。
   没找到 Request对象的成员变量创建和赋值的地方(._user) , 代码太诡异了

   python代码太松散了，可读性，维护性太差了，怀疑 django-restframework代码与python和django的兼容性。

```














