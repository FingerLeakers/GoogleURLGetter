#coding=utf-8
import requests,re
from splinter import Browser
import json
# proxies = {
# 	'http':"http://127.0.0.1:8087",
# 	'https':"http://127.0.0.1:8087"
# }
# url = "https://www.google.com.hk/search?q=intext:powered+by+dedecms&newwindow=1&safe=strict&biw=1366&bih=342&ei=0qg3VIT8Mo_98AXjuILACQ&start=290&sa=N&filter=0"
# r = requests.get(url,proxies=proxies,verify=False)
# # print r.content
# f = open('what.html','w')
# f.write(r.content)
# pattern = re.compile(r'<cite>(.*?)</cite>')
# print pattern.findall(r.content)
# # print r.content
# f.close()

url = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=intitle:powered+by+dedecms&rsz=8&start=57"
proxies = {
	'http':"http://127.0.0.1:8087",
	'https':"http://127.0.0.1:8087"
}
r = requests.get(url,proxies=proxies,verify=False)
results = json.loads(r.content)
print str(results['responseDetails']).startswith('out')




