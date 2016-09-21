#coding:utf-8
__author__ = 'zhangbin'


python -m json.tool
python -m timeit


dict
	dictMerged1=dict(dict1.items()+dict2.items())
	dictMerged2=dict(dict1, **dict2)
	dictMerged=dict1.copy()
	dictMerged.update(dict2)
