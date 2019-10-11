import urllib.request
import urllib.parse
import http.cookiejar  


# 模拟表单提交登录,当发送完post请求的时候，将cookie保存到代码中

# 创建一个cookiejar对象
cj = http.cookiejar.CookieJar()
# 通过cookiejar创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
# 根据handler创建一个opener
opener = urllib.request.build_opener(handler)

post_url = 'https://hundsonvine.com/Buyer/signin'

formdata = {
	'email': '952772885@qq.com',
	'password': '6NCV905'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}
request = urllib.request.Request(url=post_url,headers=headers)

formdata = urllib.parse.urlencode(formdata).encode()

response = opener.open(request,data=formdata)

print(response.read().decode())
print('*'*50)





get_url = 'https://hundsonvine.com/Buyer/account'

request = urllib.request.Request(url=get_url,headers=headers)
response = opener.open(request)

print(response.read().decode())