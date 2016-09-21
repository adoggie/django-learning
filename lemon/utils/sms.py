# -*- coding: UTF-8 -*-

import smtplib,traceback,os,sys,time,os.path,base64
import urllib,urllib2
SN = 'SDK-MOV-010-00421'
PWD = '134706'
MD5PWD='9E92A17D16DC171C7D3288CBFCFF0FEF'
SENDURL='http://sdk2.zucp.net:8060/z_mdsmssend.aspx'
BALANCEURL='http://sdk2.zucp.net:8060/z_balance.aspx'

	  
def send_sms(target,content):
	sendStatus = False
	failResson =''
	#content=content.decode('utf-8')[:20]
	#content= content.encode('utf8')
	try:
#		target =target.decode("utf-8").encode("")
#		如果短信内容超过500个字符,默认不发送,返回False
		if len(content)>500:
			failResson = '短信内容超过500个字符'
			return sendStatus
		querystr = "sn="+SN+ \
		           "&pwd="+MD5PWD+ \
		           "&mobile="+target+ \
		           "&content="+content.decode("utf-8").encode("gb2312")+ \
		           "&ext="+""+\
		           "&rrid="+""+\
		           "&stime="+""
		url = SENDURL+ "?"+querystr
		responseStr = urllib.urlopen(url).read()
#		responseStr = urllib.urlopen("www.dafdsf.fsadfon.com")
		try:
			result = int(responseStr)
		except TypeError:
			return sendStatus
		else:
			if result > 0:
				if(result==1):
					sendStatus = False
					failResson = '没有需要取得的数据'
				else:
					failResson = "发送成功"
					sendStatus = True
			else:
				sendStatus = False
				if(result== -2):
					failResson ='帐号/密码不正确'
				elif(result== -4):
					failResson ='余额不足'
				elif(result== -5):
					failResson ='数据格式错误'
				elif(result== -6):
					failResson ='参数有误'
				elif(result== -7):
					failResson ='权限受限'
				elif(result== -8):
					failResson ='流量控制错误'
				elif(result== -9):
					failResson ='扩展码权限错误'
				elif(result== -10):
					failResson ='内容长度长'
				elif(result== -11):
					failResson ='内部数据库错误'
				elif(result== -12):
					failResson ='序列号状态错误'
				elif(result== -13):
					failResson ='没有提交增值内容'
				elif(result== -14):
					failResson ='服务器写文件失败'
				elif(result== -15):
					failResson ='文件内容base64编码错误'
				elif(result== -17):
					failResson ='没有权限'
				elif(result== -18):
					failResson ='需等待上次的提交返回'
				elif(result== -19):
					failResson ='禁止同时使用多个接口地址'
				elif(result== -20):
					failResson ='提交过多'
				elif(result== -22):
					failResson ='Ip鉴权失败 '
				else:
					failResson='其他不明原因'
			print responseStr,failResson
			return sendStatus
	except:
		traceback.print_exc()
		return sendStatus


if __name__ == '__main__':
	send_sms("13916624477","老张,新年快乐诶!!!")