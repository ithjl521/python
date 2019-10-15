import requests



# 自己伪装头部
headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
'''
# 不带参数的get
url = 'https://www.baidu.com'

r = requests.get(url,headers=headers)

# 查看编码
print(r.encoding)

# 修改编码
r.encoding = 'utf8'
print(r.text)
'''

# 带参数的get
url = 'https://www.baidu.com/s'
data = {
	'ie':'utf8',
	'kw':'中国'
}

r = requests.get(url,headers=headers,params=data)
# 把结果写入文件
with open('baidu.html','wb') as fp:
	fp.write(r.content)



