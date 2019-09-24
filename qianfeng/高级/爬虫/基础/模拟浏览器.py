#coding=utf-8
import urllib.request
import os
import random

os.environ['http_proxy'] = ''



url = r"http://www.baidu.com"

# 模拟请求头
headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

# 设置一个请求体
req = urllib.request.Request(url,headers=headers)

# 发起请求
response = urllib.request.urlopen(req)
data = response.read()
print(data)




# 多个User-Agnet防止封IP
agnetList = ["Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
,"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"]

agnetStr = random.choice(agnetList)
req = urllib.request.Request(url)
# 向请求体里添加了User-Agnet
req.add_header("User-Agnet",agnetStr)

response = urllib.request.urlopen(req)
print(response.read())
