#coding=gbk

import urllib.request
import os

os.environ['http_proxy'] = ''

urllib.request.urlretrieve("http://www.baidu.com",filename=r"C:\Users\jiuzhou\Desktop\python\qianfeng\高级\爬虫\file\file2.html")
# urlretrieve在执行过程中，会产生一些缓存
# 清除缓存
urllib.request.urlcleanup()
