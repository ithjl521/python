import threading

# 锁对象
lock = threading.Lock()

num = 0

def run(n):
	global num
	for i in range(1000000):
		'''
		# 加锁
		lock.acquire()
	
		try:
			num = num + n
			num = num - n
		finally:
			# 释放锁
			lock.release()
		'''
		
		# 与上面代码功能相同，with lock可以自动加锁和解锁
		with lock:
			num = num + n
			num = num - n

if __name__ == "__main__":
	t1 = threading.Thread(target=run,args=(6,))
	t2 = threading.Thread(target=run,args=(9,))
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()

	
print(num)

