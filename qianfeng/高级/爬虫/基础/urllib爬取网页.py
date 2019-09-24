#coding=gbk

import urllib.request

# 向指定的url地址发起请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen("https://www.baidu.com")

# 读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
# data = response.read().decode('utf-8')

# 读取一行
# data = response.readline()

# 读取文件的全部内容，会把读取到的数据赋值给一个列表变量
# data = response.readlines()
# print(type(data))


# 将爬取到的网页写入文件
# with open(r"C:\Users\jiuzhou\Desktop\python\qianfeng\高级\爬虫\file\file1.html",'w') as f:
	# f.write(data)
	
# response 属性
# 返回当前环境的有关信息
# print(response.info())

# 返回状态码
# print(response.getcode())

# 返回当前正在爬取的url地址
# print(response.geturl())





