import threading
import time


def run(num):
	print("子线程%s启动"%(threading.current_thread().name))
	
	print("打印%d"%num)
	
	time.sleep(2)

	
	print("子线程%s结束"%(threading.current_thread().name))


if __name__ == "__main__":
	# 任何进程默认会启动一个线程，称为主线程，主线程可以启动新的子线程
	
	# current_thread() 返回当前线程的实力
	print("主线程启动--%s" %(threading.current_thread().name))
	
	# 创建子线程
	t = threading.Thread(target=run,name="runThread",args=(1,))
	t.start()
	
	# 主进程等待子线程结束
	t.join()
	
	print("主线程结束--%s" %(threading.current_thread().name))