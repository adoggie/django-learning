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


"""
