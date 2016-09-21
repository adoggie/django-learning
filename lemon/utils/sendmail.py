# -*- coding: UTF-8 -*-

import smtplib,traceback,os,sys,time,os.path,base64
from email.mime.text import MIMEText  

mailto_list=['socketref@hotmail.com','24509826@qq.com']

	  
def send_mail(to_list,sub,content,user='bin.zhang@sw2us.com',passwd='runonce',mailfrom='bin.zhang@sw2us.com', mail_host='mail.sw2us.com'):  

	me="sw2us.platform"+"<"+mailfrom+">"
	msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
	msg['Subject'] = sub  
	msg['From'] = me  
	msg['To'] = ";".join(to_list)  
	try:  
		server = smtplib.SMTP()  
		#server.debuglevel = 5 
		server.connect(mail_host)  
		server.ehlo() 
		#server.esmtp_features["auth"] = "LOGIN PLAIN"
		#user = 'bin.zhang@sw2us.com'
		#mail_pass = 'runonce'
		#print '--- to login:'
		server.login(user,passwd)  
		server.sendmail(me, to_list, msg.as_string())  
		server.close()  
		return True  
	except:
		traceback.print_exc()
		return False  
		
		
if __name__ == '__main__':  
	for n in ['autonavi.com',]:
		if send_mail(mailto_list,"just test!",n):
			print 'send ok'
		else:  
			print 'send failed'