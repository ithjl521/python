import time
import threading

# 耗时操作
def longIo(callback):
		
	def run(cb):
		print('耗时操作开始')
		time.sleep(3)
		print('耗时操作结束')
		cb('返回值')

	# 开启一个子线程来执行耗时操作，然后去执行其他请求，耗时操作结束后再通过回调函数返回	
	threading.Thread(target=run,args=(callback,)).start()
	

# 回调函数	
def finish(data):
	print('开始处理回调函数')
	print('接收到longIo响应数据：',data)
	print('结束处理回调函数')


# 一个客户端请求	
def reqA():
	print('开始A处理')
	longIo(finish)
	print('结束A处理')
	
	
# 另一个客户端请求	
def reqB():
	print('开始B处理')
	time.sleep(2)
	print('结束B处理')
	
def main():
	reqA()
	reqB()
	
if __name__ == '__main__':
	main()