def say(age):
	print('**********')
	print("hjl is a %d year old"%age)


say(-10)

def outher(func):
	def inner(age):
		if age < 0:
			age=0
		func(age)

	return inner

say = outher(say)
say(-10)

# 将函数当参数传入外函数，在内函数调用传入的函数，并且在外函数返回内涵数


