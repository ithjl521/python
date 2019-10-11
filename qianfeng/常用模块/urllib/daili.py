import urllib.request
import urllib.parse

# 27.43.188.94
# 创建handler
handler = urllib.request.ProxyHandler({'http':'27.43.188.94:9999'})

# 创建opener
opener = urllib.request.build_opener(handler)

url = 'https://www.baidu.com/s?wd=IP'

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}
request = urllib.request.Request(url,headers=headers)

response = opener.open(request)

with open('ip.html','wb') as fp:
	fp.write(response.read())

