import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json


class ZhiLianSpider(object):
	# url = 'https://sou.zhaopin.com/?jl=765&kw=python&kt=3&sf=0&st=0'
	url = 'https://sou.zhaopin.com/?'

	def __init__(self,jl,kw,start_page,end_page):
		self.jl = jl
		self.kw = kw
		self.start_page = start_page
		self.end_page = end_page
		self.items = [] # 空列表用来存放所有工作信息
	
	# 根据page拼接url，生成请求对象
	def handle_request(self,page):
		data = {
			'jl':self.jl,
			'kw':self.kw,
			'kt':page
		}
		url_now = self.url + urllib.parse.urlencode(data)
		# 构造请求对象
		headers = {
			"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
		}
		request = urllib.request.Request(url=url_now,headers=headers)
		
		return request
	
	# 解析内容
	def parse_content(self,content):
		# 构建对象
		soup = BeautifulSoup(content,'lxml')
		# 先找到所有table列表,第一个不要
		table_list = soup.select('#newlist_list_content_table > table')[1:]
		# 遍历table list依次获取每个table
		for table in table_list:
			# 获取职位名称
			job_name = table.select('.zwmc > div > a')[0].text
			# 获取公司名称
			company_name = table.select('.gsmc > a')[0].text
			# 获取职位月薪
			month_money = table.select('.zwyx')[0].text
			# 获取工作地点
			job_address = table.select('.gzdd')[0].text
			# 获取发布时间
			send_time = table.select('gxsj > span')[0].text
			
			# 组合存放到字典
			item = {
				"职位名称":job_name,
				"公司名称":company_name,
				"职位月薪":month_money,
				"工作地点":job_address,
				"发布时间":send_time,
			}
			# 存放到列表
			self.items.append(item)
		
	def run(self):
	
		for page in range(int(self.start_page),int(self.end_page) + 1):
			request = self.handle_request(page)
			# 发送请求获取内容
			content = urllib.request.urlopen(request).read()
			# 解析内容
			self.parse_content(content)
			
			
		# 将列表数据存放到文件
		string = json.dumps(self.items)
		with open('zhilian.txt','w',encoding='utf8') as fp:
			fp.write(string)
	
	
	
	

def main():
	jl = input('请输入工作地点（城市代码）：')
	kw = input('请输入工作关键字：')
	start_page = input('请输入起始页码：')
	end_page = input('请输入结束页码：')
	
		
	# 创建对象，启动爬取程序
	spider = ZhiLianSpider(jl,kw,start_page,end_page)
	spider.run()
		

if __name__ == '__main__':
	main()





