import threading
import time
from queue import Queue
import requests
from lxml import etree
import json

# 用来存放采集线程
g_crawl_list = []
# 用来存放解析线程
g_parse_list = []

class CrawlThread(threading.Thread):
	def __init__(self,name,page_queue,data_queue):
		super().__init__()
		self.name = name
		self.page_queue = page_queue
		self.data_queue = data_queue
		self.url = 'http://www.yfqp.cn/zhangzishi-w-568410-{}.htm'
		self.headers = {
			"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
		}
		
	def run(self):
		print('%s线程启动'%self.name)
		while 1:
			# if self.page_queue.empty():
				# break
		
			# 从页码队列取出页码
			page = self.page_queue.get()
			# 拼接url，发送请求
			url = self.url.format(page)	
			r = requests.get(url=url,headers=self.headers)
			
			# 将相应内容存放到data_queue
			self.data_queue.put(r.text)
			print('%s线程结束'%self.name)
			
		
class ParseThread(threading.Thread):
	def __init__(self,name,data_queue,fp,lock):
		super().__init__()
		self.name = name
		self.data_queue = data_queue
		self.fp = fp
		self.lock = lock
		
	def run(self):
		print('%s线程启动'%self.name)
		while 1:
			# if self.data_queue.empty():
				# break
			# 从data_queue取出一页数据
			data = self.data_queue.get()
			# 解析内容
			self.parse_content(data)
			print('%s线程启动'%self.name)
		
	def parse_content(self,data):
		tree = etree.HTML(data)
		# 获取所有div列表
		div_list = tree.xpath('//div[@id="article"]/div[@class="loop"]')
		
		items = []
		
		for div in div_list:
			# 获取标题
			title = div.xpath('.//div/h2/a/text()')[0]
			# 获取内容
			try:
				content = div.xpath('.//div/p/text()')[0]
			except:
				content = ''
			
			item = {
				'标题':title,
				'内容':content
			}
			
			items.append(item)
			
		# 写入文件
		self.lock.acquire()
		self.fp.write(json.dumps(items,ensure_ascii=False)+'\n')
		self.lock.release()
		
		
def create_crawl_thread(page_queue,data_queue):
	crawl_name = ['采集线程1','采集线程2','采集线程3']
	for name in crawl_name:
		tcrawl = CrawlThread(name,page_queue,data_queue)
		# 保存到列表中
		g_crawl_list.append(tcrawl)
		
def create_parse_thread(data_queue,fp,lock):
	parse_name = ['解析线程1','解析线程2','解析线程3']
	for name in parse_name:
		tparse = ParseThread(name,data_queue,fp,lock)
		# 保存到列表中
		g_parse_list.append(tparse)


def create_queue():
	# 创建页码队列
	page_queue = Queue()
	for x in range(1,11):
		page_queue.put(x)
		
	# 创建内容队列
	data_queue = Queue()
	
	return page_queue,data_queue
	
		

	

def main():
	# 创建队列
	page_queue,data_queue = create_queue()
	
	# 打开文件
	fp = open('jian.json','a',encoding='utf8')
	# 创建锁
	lock = threading.Lock()
	
	# 创建采集线程
	create_crawl_thread(page_queue,data_queue)
	# 创建解析线程
	create_parse_thread(data_queue,fp,lock)
	
	# 启动所有采集线程
	for tcrawl in g_crawl_list:
		tcrawl.start()
		
	# 启动所有解析线程
	for tparse in g_parse_list:
		tparse.start()
		
		
	# 主进程等待子线程结束
	for tcrawl in g_crawl_list:
		tcrawl.join()
	
	for tparse in g_parse_list:
		tparse.join()
		
	fp.close()
	print('主线程结束')

if __name__ == '__main__':
	main()


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

