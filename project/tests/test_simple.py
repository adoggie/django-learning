import cookielib


def rainbow(self,form):
		"""fd03058401369729668d1dc2cdcc7525
		curl  --get --include  'http://apis.baidu.com/chazhao/md5decod/md5decod?md5=b035b895aae7ea345897cac146a9eee3369c9ef1'  -H 'apikey:您自己的apikey'
		"""
		import urllib2,urllib

		cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor( cookie))


		data = 'e99a18c428cb38d5f260853678922e03'
		url = 'http://apis.baidu.com/chazhao/md5decod/md5decod?md5=%s'%data
		req = urllib2.Request(url,headers= {'apikey':'fd03058401369729668d1dc2cdcc7525'} )
		resp = opener.open(req)

		ret = resp.read()

		print ret
