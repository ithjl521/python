import threading

num = 0

# 创建一个全局的ThreadLocal对象，使每个线程有独立的存储空间
# 每个线程对ThreadLocal对象都可以读写，但是互不影响
local = threading.Local()

def run(x,n):
	x = x+n
	x = x-n


def func(n):
	# 每个线程都有一个local.x，就是线程的局部变量
	local.x = num
	for i in range(100000):
		run(local.x,n)
		
	print("%s--%d"%(threading.current_thread().name,local.x))

if __name__ == "__main__":
	t1 = threading.Thread(target=func,args=(6,))
	t2 = threading.Thread(target=func,args=(9,))
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()

	
print(num)   
