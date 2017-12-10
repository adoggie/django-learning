
## Serializer 
* 用于数据的转换: 
 python原生数据 <-> 类对象(或者model对象) 
* 用于对输入数据的验证，数据对象的生成、更新
* 用于将系统对象进行反序列化生成python 简单数据。例如：Model对象反序列之后经过json编码传递输出

序列化对象: 

```python
serializer(data={})  用于数据提交验证并得到运行数据对象
serializer(instance,data={}) 用于输入数据更新instance的操作

class User:
  def __init__(self):
    self.name = 
    self.age = 
    self.address = 

class UserSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=10)
  age = serializers.IntegerField()  

data={'name':'scott','age':20}
serializer = UserSerializer(data)    
serializer.is_valid()  验证用户提交数据
serializer.save() 创建实例 , 重载 .create() 函数

user = User()
users=queryset
serializer = UserSerializer( user,data)  验证用户提交数据并应用于user对象更新操作 , 重载 .update() 函数
serializer = UserSerializer( users,many=True)  根据User类实例创建序列化对象

JSONRender.render( serializer.data) 生成json数据
```

## 定义Serializer类

```
class ProfileSerializer(serializers.Serilizer):
  famliy = serializers.CharField()
  
class UserSerializer(serializers.Serilizer):
  name = serializers.CharField(max_length=20,required=False,validators=[])  
  profile = ProfileSerializer()  嵌套
```

## ModelSerializer 

```python
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('name','age') 
    fields = '__all__' 
    
```

## 数据验证 validation

`.is_valid(False)`验证输入数据是否符合规则，如果默认将抛出异常, `.error`属性可以获得错误说明。

#### 字段验证 field-level validation 
对某一个字段进行验证可以定义方法 `.validate_<field_name>(self,value)` ,  返回正确值 `value`或者抛出异常 `serializers.ValidationError`

```python
def validate_title(self,value):
  if 'sam' is not value:
    raise ValidationError('any error message')
  return value+'_sam'  可以修改数据值
```

#### 对象级验证 object-level validation 
定义函数`validate(self,data)`完成数据验证, 返回验证值或者异常`ValidationError`

```python
class EventSerializer(serializers.Serializer):
  def validate(self,data):
    ...
    if data.has_key('data') is False:
      return serializers.ValidationError('error message')
    return data    
```

#### 验证器 validator 
定义Serializer字段时可以添加数据验证器对象
```python
def my_validator(value):
  if error: raise serializers.ValidationError('error')
  return value
class EventSerializer():
  name = serializers.CharField(validators=[my_validator,])
```
##

## 常用方法和属性

	.data - Returns the outgoing primitive representation. 返回简单数据
	.is_valid( raise_exception=True) - Deserializes and validates incoming data. 可以抑制异常的抛出
	.validated_data - Returns the validated incoming data.
	.errors - Returns any errors during validation.
	.save() - Persists the validated data into an object instance.
	
	.intial_data 返回构造函数传入的参数data
	.instance  返回构造函数传入的 instance (一般用于数据更新 partial_update) 
	

overrides:
	.to_representation() - Override this to support serialization, for read operations.
	.to_internal_value() - Override this to support deserialization, for write operations.
	.create(validated_data) and .update(instance,validated_data) - Override either or both of these to support saving instances.


	to_representation : 格式化 对象的输出

	默认的 ModelSerializer的子类，定义Meta.model之后，ListAPIView会自动调用 每一行的 to_representation()方法，将行记录每个字段值取出，每一行就是一个  dict 对象

	serializer的validte_xxxx(value) 用于自定义处理字段数据 ， 类同与 django的form的 clean_xxx()方法
	当 .is_valid() 方法被调用时，drf 扫描所有 writable 字段的数据完整性( read_only_fields 就排除在外了) , 先使用Model的字段validator，
	再挨个检查 validate_xxx()方法是否定义。
	** 如果字段加入 read_only_fields之后，将不会调用 .validate_xxx()

