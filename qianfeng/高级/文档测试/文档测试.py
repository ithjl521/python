# coding=gbk

# ���ģ�������ȡע���еĴ���ִ�У��ϸ��ս���ģʽ����
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

# �����ĵ�����
doctest.testmod()




