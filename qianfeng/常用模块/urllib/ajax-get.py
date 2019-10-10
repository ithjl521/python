import urllib.request
import urllib.parse

url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&'

# start limit

page = int(input("请输入想要的第几页数据："))
number = 20

# 构建get参数
data = {
	'page_start':(page -1) * number,
	'page_limit':number,
}


# 将字典转换为query_string
query_string = urllib.parse.urlencode(data)

url += query_string

# 自己伪装头部
headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}


# 构建请求对象
request = urllib.request.Request(url=url,headers=headers)

# 发送请求
response = urllib.request.urlopen(request)

print(response.read())

