import time
import threading


# 耗时操作
def longIo():
	print('耗时操作开始')
	time.sleep(3)
	print('耗时操作结束')
	
	yield 'hello word'

def genCoroutine(func):
	def wrapper(*args,**kwargs):
		gen1 = func() # reqA的生成器
		gen2 = next(gen1) # longIo生成器
		
		def run(g):
			res = next(g)
			try:
				gen1.send(res) # 返回给reqA数据
			except:
				pass
			
		threading.Thread(target=run,args=(gen2,)).start()
	
	return wrapper

# 一个客户端请求
@genCoroutine	
def reqA():
	print('开始A处理')
	res = yield longIo()
	print('接收到longIo响应数据：',res)
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