import requests

# 必应翻译

url = 'https://www.bing.com/tlookupv3?isVertical=1&&IG=68A1788F71EB440E83B1199EBA3F4BDA&IID=translator.5028.2'

formdata = {
	'from': 'en',
	'to': 'zh-Hans',
	'text': 'wolf',
}

# 自己伪装头部
headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

r = requests.post(url=url,headers=headers,data=formdata)
print(r.text)

