#coding=utf-8
import requests
import json
import sys
import threading
import socket
import time
import re
import random
class GoogleURLProvider():
	#构造函数
	def __init__(self,proxies,keywords):
		self.keywords = keywords
		self.apiurl = "https://ajax.googleapis.com/ajax/services/search/web"
		self.proxies = proxies
	#加了代理的request
	def getRequest(self,url):
		return requests.get(url,proxies=self.proxies,verify=False,timeout=3)

	#获取start页的全部url信息
	def getUrls(self):
		ret_list = []
		tmp_list = []
		pageCount = 0
		
		while True:
			print pageCount
			url = "{apiurl}?v=1.0&q={keywords}&rsz=8&start={pageCount}".format(apiurl=self.apiurl,keywords=self.keywords,pageCount=pageCount)
			try:
				r = self.getRequest(url)	
				results = json.loads(r.text)
				# print results['responseData']
				# print results['responseDetails']
				if str(results['responseDetails']).startswith("out"):
					print 'Job Completed'
					break
				if not results:
					continue
				#google做出了限制
				if str(results['responseData']).startswith('Suspected Terms of Service Abuse'):
					time.sleep(random.random()*10)
					continue
				infos = results['responseData']['results']
				if infos:
					for i in infos:
						tmp_list.append(i['url'])
				pageCount += 1
			except Exception, e:
				print e
				time.sleep(1)
				continue
			time.sleep(random.random()*12)
		ret_list = ret_list + tmp_list
		return ret_list

if __name__ == '__main__':
	f = open("struts2.txt",'a')
	keyfile = open('dict.txt','r')

	proxies = {
		'http':"http://127.0.0.1:8087",
		'https':"http://127.0.0.1:8087"
	}
	#keywords = "intext:Powered by Discuz"
	#keywords = "intext:Powered by DedeCMS"
	#keywords = "inurl:cgi-bin filetype:sh	
	keywords_list = [
		"inurl:Index.action",
		"inurl:CarrierImage.action"
		"inurl:Catalog.action",
		"inurl:ClearWorkspace.action",
		"inurl:ClientPresignup.action",
		"inurl:CompanyFwdAction_indexSimple.action",
		"inurl:ConferenceDetail.action",
		"inurl:ConferenceList!searchConferenceList.action",
		"inurl:ConferencePresignup.action",
		"inurl:Conferences.action"
	]	
	# keys = keyfile.readlines()
	for keywords in keywords_list:
		print keywords
		urlprovider = GoogleURLProvider(proxies,keywords)
		res = urlprovider.getUrls()
		for x in set(res):
			f.write('%s\n' % x)
	# #---------------正则匹配-----------------------------
	# pattern = re.compile(r'http[s]?://(.*?)/')
	# tmp_set = set()
	# for x in res:
	# 	x = pattern.findall(x)
	# 	tmp_set.add(x[0])
	# for i in tmp_set:
	# 	f.write("%s \n" % i)

	f.close()
    #---------------原生存储-----------------------------
	# for x in res:
	# 	f.write("%s \n" % x)
	# f.close()

