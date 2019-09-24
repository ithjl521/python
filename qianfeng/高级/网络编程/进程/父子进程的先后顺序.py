from multiprocessing import Process

from time import sleep


def run(str):
	print("启动子进程")
	sleep(3)
	print("子进程结束")

if __name__ == '__main__':
	print("主（父）进程启动")

	p = Process(target=run,args=("word",))
	p.start()

	# 让子进程结束以后父进程再结束
	p.join()

	# 如果不等待，父进程的结束不会影响子进程
	print("父进程结束")