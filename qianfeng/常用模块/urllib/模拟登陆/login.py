import urllib.request
import urllib.parse

url = 'https://hundsonvine.com/Buyer/account'

# 自己伪装头部
headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
	'Cookie': '_ga=GA1.2.1234271060.1552532125; PHPSESSID=qirb9dgpjhlet8vgl1geioqu16; _gid=GA1.2.945961828.1570585533; accessId=573072c0-c7e2-11e9-8632-3f118adb355e; qimo_seosource_573072c0-c7e2-11e9-8632-3f118adb355e=%E7%AB%99%E5%86%85; qimo_seokeywords_573072c0-c7e2-11e9-8632-3f118adb355e=; href=https%3A%2F%2Fhundsonvine.com%2F; pageViewNum=2'
}


# 构建请求对象
request = urllib.request.Request(url=url,headers=headers)

# 发送请求
response = urllib.request.urlopen(request)

with open('a.html','wb') as fb:
	fb.write(response.read())


