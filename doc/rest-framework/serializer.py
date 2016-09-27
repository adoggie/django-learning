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

"""
