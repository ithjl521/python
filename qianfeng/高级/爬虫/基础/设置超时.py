#coding=gbk
import urllib.request
import os

# 如果网页长时间未响应，系统判定超时，无法爬取
for i in range(1,100):
	try:
		response = urllib.request.urlopen("http://www.baidu.com",timeout=0.5)
	except:
		print("请求超时")
