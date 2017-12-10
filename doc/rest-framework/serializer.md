
## Serializer 
* 用于数据的转换: 
 python原生数据 <-> 类对象(或者model对象) 
* 用于对输入数据的验证，数据对象的生成、更新
* 用于将系统对象进行反序列化生成python 简单数据。例如：Model对象反序列之后经过json编码传递输出

序列化对象: 

```python
serializer(data={})  用于数据提交验证并得到运行数据对象
serializer(instance,data={}) 用于输入数据更新instance的操作


JSONRender.render( serializer.data) 生成json数据
```

## 定义Serializer类

```
class UserSerializer(serializers.Serilizer):
  name = serializers.CharField(max_length=20)  
```

## 数据验证 validation

`.is_valid(False)`验证输入数据是否符合规则，如果默认将抛出异常, `.error`属性可以获得错误说明。

#### 字段验证 field-level validation 



## 常用方法和属性

	.data - Returns the outgoing primitive representation. 返回简单数据
	.is_valid( raise_exception=True) - Deserializes and validates incoming data. 可以抑制异常的抛出
	.validated_data - Returns the validated incoming data.
	.errors - Returns any errors during validation.
	.save() - Persists the validated data into an object instance.

overrides:
	.to_representation() - Override this to support serialization, for read operations.
	.to_internal_value() - Override this to support deserialization, for write operations.
	.create() and .update() - Override either or both of these to support saving instances.


	to_representation : 格式化 对象的输出

	默认的 ModelSerializer的子类，定义Meta.model之后，ListAPIView会自动调用 每一行的 to_representation()方法，将行记录每个字段值取出，每一行就是一个  dict 对象

	serializer的validte_xxxx(value) 用于自定义处理字段数据 ， 类同与 django的form的 clean_xxx()方法
	当 .is_valid() 方法被调用时，drf 扫描所有 writable 字段的数据完整性( read_only_fields 就排除在外了) , 先使用Model的字段validator，
	再挨个检查 validate_xxx()方法是否定义。
	** 如果字段加入 read_only_fields之后，将不会调用 .validate_xxx()

