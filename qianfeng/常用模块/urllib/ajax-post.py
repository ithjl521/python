import urllib.request
import urllib.parse


url = 'https://hundsonvine.com/Goods/getGoodsList'

page = input("请输入查询的第几页：")
size = input("请输入查询多少条：")

form_data = {
	'page': page,
	'page_size': size
}

# 自己伪装头部
headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}


# 构建请求对象
request = urllib.request.Request(url=url,headers=headers)
# 处理表单数据
form_data = urllib.parse.urlencode(form_data).encode()

response = urllib.request.urlopen(request,data=form_data)


print(response.read().decode())



