import requests

url = 'http://www.yfqp.cn/zhangzishi-w-568410-30.htm'

headers = {
			"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

r = requests.get(url=url,headers=headers)

print(r.text)
