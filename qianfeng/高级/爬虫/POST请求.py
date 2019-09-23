#coding=gbk

import urllib.request
import urllib.parse

url = "http://www.test.com"

# 将要发送的数据合成一个字典
# 字典的键去网址里找，一般为input标签的name属性值
data = {
	"username":"hjl"
	"password":"admin123"
}

# 对要发送的数据进行打包(编码很重要)
postData = urllib.parse.urlencode(data).encode("utf-8")

# 请求体
req = urllib.request.Request(url,data=postData)
#请求
req.add_header("User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")

response = urllib.request.urlopen(req)

print(response.read())

