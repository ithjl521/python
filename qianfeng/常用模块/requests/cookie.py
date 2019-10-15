import requests

# 模拟登陆

# 如果碰到会话相关问题，首先要创建一个会话
# 往下所有操作都通过s进行访问
s = requests.Session()

post_url = 'https://hundsonvine.com/Buyer/signin'

headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

formdata = {
	'email': '952772885@qq.com',
	'password': '6NCV905'
}
s.post(url=post_url,headers=headers,data=formdata)


get_url = 'https://hundsonvine.com/Buyer/account'
r = s.get(url=get_url,headers=headers)
print(r.text)


