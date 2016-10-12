# coding: utf-8
from django.db.models.query import QuerySet

__author__ = 'chengchaojie'

import json
import datetime

def clean_not_match_list(func):
	def _clean_not_match_list(self, arg1, arg2):
		if self.clean_flag:
			self.result = {
				"valid": True,
				"object": None,
				"not_match": []
			}
			self.clean_flag = False

		re = func(self, arg1, arg2)
		return re

	return _clean_not_match_list


class JsonConvert:
	def __init__(self):
		self.all_match = True
		self.object = None
		self.not_match = [1, 2, 3]

	def clean_not_match_list(self):
		self.not_match = []

	def __set_object_value(self, json_obj, obj):
		for item in json_obj:
			if hasattr(obj, item):
				value = json_obj[item]

				if isinstance(value, dict):
					self.__set_object_value(value, getattr(obj, item))
				else:
					setattr(obj, item, value)

			else:
				self.all_match = False
				self.not_match.append(item)

		return self.all_match

	def set_object_value(self, json_obj, obj):

		self.clean_not_match_list()

		return self.__set_object_value(json_obj, obj)

	def json_to_object(self, json_str, obj):

		self.object = obj
		json_obj = json.loads(json_str)

		return self.set_object_value(json_obj, obj)


def json_dict_mapping(obj_dict, mapping_fields, mapping_all_field=True):
	if not isinstance(obj_dict, dict):
		return None

	result = {}
	if mapping_all_field:
		for key in obj_dict:
			if key in mapping_fields:
				result[mapping_fields.get(key)] = obj_dict.get(key)

			else:
				result[key] = obj_dict.get(key)

		return result

	else:
		for key in mapping_fields:
			if mapping_fields not in obj_dict:
				return None

			obj_dict[mapping_fields.get(key)] = obj_dict.pop(key)

		return obj_dict


def json_mapping(obj_dict_list, mapping_fields, mapping_all_field=True):
	if obj_dict_list is None and not isinstance(obj_dict_list, list) \
			and not isinstance(obj_dict_list, QuerySet) or len(obj_dict_list) == 0:
		return []

	result = []
	for obj_dict in obj_dict_list:
		result.append(json_dict_mapping(obj_dict, mapping_fields, mapping_all_field))

	return result


def convert_dict_boolean(dict_map, index=None):
	if index is not None and isinstance(index, list):
		for k in index:
			v = dict_map.get(k)
			if isinstance(v, bool):
				if v:
					dict_map[k] = 1
				else:
					dict_map[k] = 0
		return dict_map

	for k in dict_map:
		v = dict_map[k]
		if isinstance(v, bool):
			if v:
				dict_map[k] = 1
			else:
				dict_map[k] = 0

	return dict_map


def convert_obj_boolean(obj, index=None):
	result = obj.__dict__
	if index is not None and isinstance(index, list):
		for k in index:
			v = result.get(k)
			if isinstance(v, bool):
				if v:
					result[k] = 1
				else:
					result[k] = 0
		return result

	for k in result:
		v = result[k]
		if isinstance(v, bool):
			if v:
				result[k] = 1
			else:
				result[k] = 0

	return result


class Book:
	def __init__(self):
		self.book_name = None
		self.price = None
		self.person = Person()
		self.book_store = BookStore()


class Person:
	def __init__(self):
		self.person_name = None
		self.age = None


class BookStore:
	def __init__(self):
		self.address = None
		self.store_name = None


if __name__ == '__main__':
	bookstr = {
		"book_name": "Python Cookie",
		"price": 30,
		"person": {
			"person_name": "John",
			"age": 17
		},
		"book_store": {
			"store_name": "book_sea",
			"address": "长宁路300号"
		}
	}

	test_prfile = "/Users/chengchaojie/01_Person/03_Projects/98_SVN/lemon/trunk/test/7b3b49499dda49ff94fa1026af761fa8.profile"
	sss = open(test_prfile, 'r')

	dd = sss.read()

	dicts = json.loads(dd)



	strs = json.dumps(bookstr)

	jto = JsonConvert()
	r = jto.json_to_object(strs, Book())

	pass
