from time import sleep


def run():
	while True:
		print("word")
		sleep(1.2)

if __name__ == '__main__':
	while True:
		print("hello")
		sleep(1)

	# 不会执行到run方法，只有上面的循环结束才可以执行
	run()