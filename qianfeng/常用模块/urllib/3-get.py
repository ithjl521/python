import urllib.request
import urllib.parse

word = input('请输入你要搜索的内容：')
url = 'https://www.baidu.com/s?'

# 参数写成字典
data = {
	'ie':'utf-8',
	'wd':word,
}

query_string = urllib.parse.urlencode(data)

url += query_string

# 发送请求
response = urllib.request.urlopen(url)

print(url)
print(response.read())






