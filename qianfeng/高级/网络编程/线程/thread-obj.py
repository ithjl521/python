import threading
from time import sleep

'''
面向对象的方法创建线程
'''

class SingThread(threading.Thread):

	def __init__(self,name,a):
		super().__init__()
		self.name = name
		self.a = a
		
	# 重写父类方法
	def run(self):
		print('线程名字是%s，接收参数是%s'%(self.name,self.a))
		for x in range(1,6):
			print("我在唱七里香")
			# sleep(0.1)
			

class DanceThread(threading.Thread):

	def run(self):
		for x in range(1,6):
			print("我在跳街舞")
			# sleep(0.1)
			

			
def main():
	tsing = SingThread('sing','八戒')
	tdance = DanceThread()
	
	tsing.start()
	tdance.start()
	
	tsing.join()
	tdance.join()
	
	print('主线程和子线程全部结束')
	
	
if __name__ == '__main__':
	main()
