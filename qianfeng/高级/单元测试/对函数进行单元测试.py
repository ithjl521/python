# coding=gbk

# 单元测试：
# 作用：用了对一个哈数，一个类，一个模块进行正确性校验工作

# 结果：
# 1、单元测试通过，说明我们测试的函数功能正常
# 2、不通过，说明函数功能有bug或者要么测试条件有误


def mySum(x,y):
	return x+y

	
def mySub(x,y):
	return x-y
	
print(mySum(1,2))