'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
'''

from multiprocessing import Process

from time import sleep


def run(str):
	while True:
		print(str)
		sleep(1.2)

if __name__ == '__main__':
	print("主（父）进程启动")

	# 创建一个进程（子进程）
	# target 说明进程执行的任务
	# args 是run函数的参数，是一个元组
	p = Process(target=run,args=("word",))

	# 启动进程
	p.start()

	while True:
		print("hello")
		sleep(1)

	


