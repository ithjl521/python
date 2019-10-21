import time
import threading

gen=None

# 耗时操作
def longIo():
		
	def run():
		print('耗时操作开始')
		time.sleep(3)
		try:
		
			global gen
			gen.send('success')
		except:
			pass
	
	
	threading.Thread(target=run).start()
	

def genCoroutine(func):
	def wrapper(*args,**kwargs):
		global gen
		gen = func(*args,**kwargs)
		next(gen)
	
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