import urllib.request
import urllib.parse

url = 'http://www.baidu.com'


# response = urllib.request.urlopen(url)
# print(response.read().decode())

# 自己伪装头部
headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}


# 构建请求对象
request = urllib.request.Request(url=url,headers=headers)

# 发送请求
response = urllib.request.urlopen(request)

print(response.read())





