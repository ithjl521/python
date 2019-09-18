# coding=gbk

# 这个模块可以提取注释中的代码执行，严格按照交互模式输入
import doctest  


def mySum(x,y):
	'''
	get the sum from x and y
	:param x : firstNum
	:param y : secondNum
	:return : sum
	
	example:
	>>> print(mySum(1,2))
	3
	'''
	return x+y
	
	
print(mySum(1,2))

# 进行文档测试
doctest.testmod()




