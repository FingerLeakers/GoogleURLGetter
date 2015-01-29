#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import time
import urllib
import random
class GoogleURLGetter():
	def __init__(self,proxies,headers):
		self.proxies = proxies
		self.headers = headers
	def getUrl(self,keywords):
		page_count = 0
		first_page = []
		all_urls = []
		tmp_res = []
		flag = True
		f = open('user_agents')
		user_agents = f.read().split('\n')
		f.close()
		while True:
			try:
				keywords = keywords.replace(" ","+")
				print 'keywords:%s' % keywords
				length = len(user_agents)
				index = random.randint(0,length-1)
				self.headers['User-Agent'] = user_agents[index]
				print self.headers
				url = "https://www.google.com.hk/search?q={keywords}&newwindow=1&safe=strict&biw=1366&bih=342&ei=0qg3VIT8Mo_98AXjuILACQ&start={page_count}&sa=N&filter=0".format(keywords=keywords,page_count=page_count)
				r = requests.get(url,proxies=self.proxies,headers=headers,verify=False,timeout=13)
				pattern = re.compile(r'<cite class="_Rm">(.*?)[>]?</cite>')
				tmp_res = pattern.findall(r.content)
				f = open('what.html','w')
				f.write(r.content)
				f.close()
				if page_count == 0:   #将第一页的内容保存
					first_page = tmp_res  
				#如果不是第一页的内容，则开始采集
				if (tmp_res != first_page and page_count != 0) or flag:
					urls = []   
					for x in tmp_res:
						# clear_url = x.replace("<b>","").replace("</b>","")
						# clear_url = clear_url[0:clear_url.index("/")]
						# urls.append(clear_url)
						urls.append(x)
					all_urls.extend(urls)
					print all_urls 
				else:
					print 'break'
					break
				page_count += 10
				flag = False
			except Exception, e:
				print e
				continue
		return all_urls

if __name__ == '__main__':
	proxies = {
		'http':"http://127.0.0.1:8087",
		'https':"http://127.0.0.1:8087"
	}
	headers = {'User-Agent':'',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':'gzip,deflate',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
		'Host':'www.google.com.hk'
	}
	urlgetter = GoogleURLGetter(proxies,headers)
	res = urlgetter.getUrl('filetype:action')
	f = open('data.txt','a')
	if len(res) != 0:
		for x in res:
			f.write("%s\n" % x)
	f.close()


