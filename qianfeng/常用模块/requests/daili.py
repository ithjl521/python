import requests

url = 'https://www.baidu.com/s?wd=IP'

proxy = {
	'http':'http://58.253.156.230:9999'
}

headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

r = requests.get(url,headers=headers,proxies=proxy)

print(r.text)
