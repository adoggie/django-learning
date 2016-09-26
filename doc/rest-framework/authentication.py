#coding:utf-8
"""
restframework携带三种认证方法:
	BasicAuthentication
	SessionAuthentication
	TokenAuthentication


rest 缺省开启的认证方式
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
"""

"""
BasicAuthentication :
	每一次api请求都携带用户名和密码， 从http头部获取认证信息，包含登陆用户名和口令( base64编码)，到数据库验证用户是否合法，并返回user
	"
	WWW-Authenticate: Basic realm="api"
	"
	request.user  将被设置
	request.auth  为None

SessionAuthentication：
	简单的检查request.user是否为空或者是否激活 is_active ,如果已登陆则返回user
	request.user  将被设置
	request.auth  为None
	当restframwework与django页面登陆验证共享时，这是个简单的方法，django页面的登陆结果在rest中直接使用 。
	SesionAuthentication 一般都在浏览器页面的ajax操作的场景 ， rest使用django的用户认证结果，但必须注意 csrf 问题
	为保证安全，每个ajax请求需要携带 crsf token

TokenAuthentication
	这种认证方式是，为当前存在的用户User创建一个token，并保存在数据库中，以后用户登陆就使用此token作为凭证。
	生成token、发布token和管理token是个问题 。

	令牌认证方式，每一次webapi请求都会携带一个认证token
	使用时必须加入 'rest_framework.authtoken' 到 INSTALLED_APPS 列表 ，并且需要同步数据库，其将创建用户user相关的token表

	"Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"

	request.user user
	request.auth  rest_framework.authtoken.models.Token

"""

"""
代码中使用认证方式

class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

此view被请求前进行 SessionAuthentication认证，如果把失败则进行用户名＋口令方式认证

"""

"""

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def example_view(request, format=None):
	...

"""

















