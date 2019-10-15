import requests
from bs4 import BeautifulSoup
import urllib.request

'''
登录古诗文网
将验证码保存到本地手动验证
'''

headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

# 下载验证码到本地
def download_code(s):
	url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
	r = s.get(url=url,headers=headers)
	soup = BeautifulSoup(r.text,'lxml')
	# 得到图片链接
	image_src = 'https://so.gushiwen.org'+soup.find('img',id='imgCode')['src']
	# 保存图片
	# urllib.request.urlretrieve(image_src,'code.png')
	r.image = s.get(image_src,headers=headers)
	with open('code.png','wb') as fp:
		fp.write(r.image.content)
	
	# 查找表单需要的两个参数
	__VIEWSTATE = soup.find('input',id='__VIEWSTATE')['value']
	__VIEWSTATEGENERATOR = soup.find('input',id='__VIEWSTATEGENERATOR')['value']
	
	return __VIEWSTATE,__VIEWSTATEGENERATOR
	
def login(view,viewg,s):
	post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
	
	# 提示用户输入验证码
	code = input('请输入验证码：')
	
	formdata = {
		'__VIEWSTATE': view,
		'__VIEWSTATEGENERATOR': viewg,
		'from': 'http://so.gushiwen.org/user/collect.aspx',
		'email': '245180912@qq.com',
		'pwd': 'admin123',
		'code': code,
		'denglu': '登录',
	}
	
	r = s.post(url=post_url,headers=headers,data=formdata)
	
	with open('gushiwen.html','w',encoding='utf8') as fp:
		fp.write(r.text)
	

def main():
	# 创建会话(因为该网站的验证码，不是每次都一样，所以要在同一个会话里面。一般网站都是每次随机)
	s = requests.Session()

	# 下载图片
	view,viewg = download_code(s)
	
	#向post地址发送登录请求
	login(view,viewg,s)
	
	
if __name__ == '__main__':
	main()

