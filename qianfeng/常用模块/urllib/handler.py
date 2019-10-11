import urllib.request
import urllib.parse

url = 'https://hundsonvine.com'

headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

# 创建handler
handler = urllib.request.HTTPHandler()
# 通过handler创建一个opener
opener = urllib.request.build_opener(handler)

# 构建请求对象
request = urllib.request.Request(url,headers=headers)

# 发送请求
response = opener.open(request)

print(response.read().decode())



