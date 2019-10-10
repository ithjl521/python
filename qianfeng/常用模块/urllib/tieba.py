import urllib.request
import urllib.parse
import os

# 百度贴吧

url = 'http://tieba.baidu.com/f?ie=utf-8&'

ba_name = input('请输入吧名：')
start_page = int(input('请输入要爬取的起始页码：'))
end_page = int(input('请输入要爬取的结束页码：'))

# 创建文件夹
if not os.path.exists(ba_name):
	os.mkdir(ba_name)

for page in range(start_page,end_page+1):
	# page就是当前页
	# 拼接url
	data = {
		'kw':ba_name,
		'pn':(page - 1)*50
		
	}
	
	data = urllib.parse.urlencode(data)
	url_t = url + data
	
	#print(url_t)
	
	# 自己伪装头部
	headers = {
		"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
	}


	# 构建请求对象
	request = urllib.request.Request(url=url_t,headers=headers)

	# 发送请求
	response = urllib.request.urlopen(request)
	
	# 生成文件名
	filename = ba_name + '_' + str(page) + '.html'
	# 拼接文件路径
	filepath = ba_name + '/' + filename
	
	# 写内容
	with open(filepath,'wb') as fp:
		fp.write(response.read())
		
	print("第%s页下载结束"%page)
	

