from functools import reduce

# map()
# 原型 map(fn,lad)
# 参数一是函数，参数二是序列

# 功能：将传入的函数依次作用在序列的每一个元素，并把结果作为新的Iterator返回


# 将单个字符转换成对应的字面量整数
def char2int(char):
	return {"0":0,"1":1,"2":2,"3":3}[char]

	
list1 = ["1","2","0"]
res = map(char2int,list1)	
print(list(res))






#reduce(fn,lsd)
# 参数一是函数，参数二是列表
# 功能：一个函数作用在序列上，这个函数必须接受两个参数，
# reduce把结果继续和序列的下一个元素累计运算

# 求一个序列的和
list2 = [1,2,3,4,5]

def mySum(x,y):
	return x+y
	
r = reduce(mySum,list2)
print(r)




# 将字符串转成对应字面量数字
def str2int(str):
	def fc(x,y):
		return x*10+y
		
	def fs(char):
		return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[char]
		
	return reduce(fc,map(fs,list(str)))
	

a = str2int("12365")
print(a)
print(type(a))
	
	
	
	
	
	
	