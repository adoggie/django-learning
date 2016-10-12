#coding:utf-8

"""
BaseSerializer

	.data - Returns the outgoing primitive representation.
	.is_valid() - Deserializes and validates incoming data.
	.validated_data - Returns the validated incoming data.
	.errors - Returns any errors during validation.
	.save() - Persists the validated data into an object instance.

overrides:
	.to_representation() - Override this to support serialization, for read operations.
	.to_internal_value() - Override this to support deserialization, for write operations.
	.create() and .update() - Override either or both of these to support saving instances.


to_representation : 格式化 对象的输出

默认 的 ModelSerializer的子类，定义Meta.model之后，ListAPIView会自动调用 每一行的 to_representation()方法，将行记录每个字段值取出，每一行就是一个  dict 对象

serializer的
	validte_xxxx(value) 用于自定义处理字段数据 ， 类同与 django的form的 clean_xxx()方法
	当 .is_valid() 方法被调用时，drf 扫描所有 writable 字段的数据完整性( read_only_fields 就排除在外了) , 先使用Model的字段validator，
	再挨个检查 validate_xxx()方法是否定义。
	** 如果字段加入 read_only_fields之后，将不会调用 .validate_xxx()
"""
