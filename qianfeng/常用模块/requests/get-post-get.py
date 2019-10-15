import requests
from bs4 import BeautifulSoup
import time
'''
先get请求获取token，在post请求登录，最后get请求获取数据
'''

s = requests.Session()

# 访问登陆页面，获取登录所需要的参数
get_url = 'http://account.chinaunix.net/login'
headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
r = requests.get(get_url,headers=headers)


soup = BeautifulSoup(r.text,'lxml')
# 获取token
token = soup.find('input',type='hidden')['value']
# 向指定post发送请求
post_url = 'http://account.chinaunix.net/login/login'
# 当前时间戳，毫秒级
timestamp = int(round(time.time() * 1000))
formdata = {
	'username': 'ithjl521',
	'password': 'admin123',
	'_token': token,
	'_t': timestamp
}

# 发起登录请求
r_post = s.post(url=post_url,headers=headers,data=formdata)
# print(r_post.text)


# 访问登陆后的页面
member_url = 'http://account.chinaunix.net/ucenter/user/index'
r = s.get(url=member_url,headers=headers)
print(r.text)


