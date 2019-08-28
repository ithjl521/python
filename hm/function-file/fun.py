

def multiple_table():
	"""函数注释写这里"""

	row=1
	while row<=9:
		col=1
		while col<=row:
			print("%d * %d = %d"%(col,row,row*col),end='\t')
			col+=1

		print()
		row+=1
	

def say_hello():
	"""函数上方必须有两行空行"""

	i=0
	while i<3:
		print('hello')
		i+=1


def sum_num1_num2(num1,num2):

	"""数字求和
	
	:param num1:第一个数字
	:param num2：第二个数字
	"""

	sum = num1 + num2
	return sum