import urllib.request
import urllib.parse
from lxml import etree
import json

# 定义一个列表用于存放最终的内容
duanzi_list = []

def handle_request(url):
	# 构造请求对象
	headers = {
		"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
	}
	
	request = urllib.request.Request(url=url,headers=headers)
	return request

		
def parse_content(content):
	tree = etree.HTML(content)
	# 获取ul下class不为ad的li列表
	li_list = tree.xpath('//ul[@class="list-box"]/li[not(@class="ad")]')
	# 遍历列表
	for li in li_list:
		title = li.xpath('.//h2/text()')[0]
		content_child = li.xpath('.//div[@class="content"]/a//text()')[0]
		
		# 放入到一个字典
		item = {
			'title':title,
			'content_child':content_child
		}
		
		# 加入到列表
		duanzi_list.append(item)
	
def main():
	start_page = int(input("输入起始页码："))
	end_page = int(input("输入结束页码："))
	
	url = 'http://www.haoduanzi.com/category/?11-{}.html'
	# 循环选取的页数
	for page in range(start_page,end_page + 1):
		url_l = url.format(page)
		# 构造请求对象
		request = handle_request(url_l)
		
		# 发送请求获取内容
		content = urllib.request.urlopen(request).read().decode()
		# 解析内容
		parse_content(content)
		# 将内容json编码后写入到文件
		string = json.dumps(duanzi_list,ensure_ascii=False)
		
		with open('duanzi.txt','a',encoding='utf8') as fp:
			fp.write(string)
	
	
if __name__ == "__main__":
	main()
	
