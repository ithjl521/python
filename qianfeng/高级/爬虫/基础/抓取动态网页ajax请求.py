
import urllib.request
import ssl
import json

def ajaxCrawler(url):
	headers = {
		"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
	}
	req = urllib.request.Request(url,headers=headers)
	
	# 使用ssl创建未验证的上下文
	context = ssl._create_unverified_context()
	
	response = urllib.request.urlopen(req,context=context)
	
	jsonStr = response.read().decode("utf-8")
	
	# 判断返回的是否是json字符串，如果是，做转化处理
	try:
		jsonData = json.loads(jsonStr)
	except ValueError:
		return jsonStr
	
	return jsonData
	
	
url = "https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=60"
info = ajaxCrawler(url)
print(type(info))
print(info)


for i in (1,11):
	url = "https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start="+str(i*20)
	info  = ajaxCrawler(url)
	print(len(info))
