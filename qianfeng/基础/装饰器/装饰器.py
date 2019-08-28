# 是一个闭包，把一个函数当做参数返回


def fun1():
	print('hello word')


def outer(func):
	def inner():

		print('************')
		func()

	return inner


f = outer(fun1)
f()



