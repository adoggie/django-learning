#coding:utf-8

# api-doc export to markdown

import json


def print_parameters(nodes,indent=1):
	text =''
	for node in nodes:
		text+='\t'*indent + u'\t%10s:\t%10s\t[%s]\t --:%s\n'%( node.get('name'),
		                               '('+node.get('type')+')',
		                               node.get('default','unset'),
		                               node.get('description','null'))
		children = node.get('children')
		if children:
			text+=print_parameters(children,indent+1)
	return text

def markdown_apidoc(doc,idx=0):
	from webapi.models import ApiDoc
	module = doc.module
	app = doc.module.app
	text = '------------------\n\n'
	idx+=1
	text+=u'##%s. %s\n'%(idx,doc.name)

	text+=u'###Ver\n'
	text+=u'\t%s\n'%doc.ver
	text+=u'###Description\n'
	text+=u'\t%s\n'%doc.description
	text+=u'###Request\n\n'
	text+=u'####URL:\t%s\n'%doc.url
	text+=u'####Method:\t%s\n'%doc.method
	text+=u'####Headers:\n'

	headers = json.loads(doc.headers)
	for header in headers:
		text+=u'\t\t%s:\t%s\t--%s\n'%(header.get('name'),
		                              header.get('default'),
		                              header.get('description'))

	paramters = json.loads(doc.paramters)
	text+=u'####Parameters:\n'
	text+=print_parameters(paramters)

	text+=u'###Response\n'
	text+=u'####Headers:\n'
	text+=u'####Status: %s \n'%(doc.resp_status,)

	headers = json.loads(doc.resp_headers)
	for header in headers:
		text+=u'\t\t%s:\t%s\t`%s`\n'%(header.get('name'),
		                              header.get('default'),
		                              header.get('description'))

	text+=u'####Data:\n'
	paramters = json.loads(doc.resp_data)
	text+=print_parameters(paramters)

	text+=u'###Examples:\n'
	text+=u'\t%s\n'%(doc.examples or '')

	text+=u'###Remarks:\n'
	text+=u'\t%s\n'%(doc.comment or '')

	text+='\n'*2
	return text



def markdown_html(doc_ids):
	import markdown
	from webapi.models import ApiDoc
	# print isinstance(doc_ids,list)
	# if type(doc_ids) not in ( 'list','tuple'):
	# 	doc_ids = [doc_ids,]

	content =''
	for idx,doc_id in enumerate(doc_ids):
		doc = ApiDoc.objects.get(id = doc_id)
		content += markdown_apidoc(doc,idx)

	html = markdown.markdown(content)
	return html

def test():
	data = [{"description": " 0 - succ ; others - fail", "default": 0, "state": "open", "type": "int", "id": 1, "name": "status"}, {"description": "", "default": "0", "state": "open", "type": "string", "id": 2, "name": "errcode"}, {"description": "", "default": "", "state": "open", "type": "string", "id": 3, "name": "errmsg"}, {"description": "", "default": "", "children": [{"name": "token", "default": "", "_parentId": 4, "state": "open", "type": "string", "id": "0b027d4b_cabe_4aee_9d75_509d835f46c0", "description": "\u7528\u6237\u767b\u5f55\u4ee4\u724c"}], "state": "open", "type": "string", "id": 4, "name": "result"}]
	text = print_parameters(data)
	print text

if __name__ == '__main__':
	test()