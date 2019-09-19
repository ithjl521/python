#coding=gbk

import re

'''
字符串切割
'''
str1 = "hjl   is a good    man"
print(re.split(r" +",str1))



'''
re.finditer函数
原型re.finditer(pattern,string,flags=0)
patter：匹配的正则表达式
string：要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回一个迭代器
'''

str2 = "hjl is a good man! hjl is a nice man!"
d = re.finditer(r"(hjl)",str2)
while True:
	try:
		l = next(d)
		print(l)
	except:
		break


'''
字符串替换和修改
re.sub(pattern,repl,string,count=0,flags=0)
re.subn(pattern,repl,string,count=0,flags=0)	
pattern  正则表达式
repl 	  指定的用来替换的字符串
string 		目标字符串
count=0 	最多替换次数
flags=0	
功能：在目标字符串中以正则表达式的规则匹配字符串，再把它们替换成指定的字符串，
	可以指定替换的次数。如果不指定，全部替换
区别：前者返回被替换成的字符串。
	后者返回一个元组，元组第一个元素是被替换成的字符串，第二个元素是被替换次数
'''
str5 = 'hjl is a good good good man'
print(re.sub(r'(good)','nice',str5))
print(re.subn(r'(good)','nice',str5))		
		
		

'''
分组：
概念：除了简单的判断是否匹配之外，正则表达式还有提取了子串的功能，用()小括号表示的就是提取分组。
'''		
str3 = "010-23458712"
m = re.match(r"((?P<first>\d{3})-(?P<last>\d{8}))",str3)
# 使用序号获取对应组的信息，group(0)一直代表原始字符串
print(m.group(0))
print(m.group(1))
print(m.group('first')) # 通过自己取名的组获取数据
print(m.group(2))

# 查看匹配的各组的情况
print(m.groups())
		
		
		
		
'''
编译：当我们使用正则表达式时，re模块会做两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
re.compile(pattern,flags=0)
	pattern:要编译的正则表达式
'''	

pat = r"^1(([3578]\d)|(47))\d{8}$"
# 编译成正则对象	
re_telephone = re.compile(pat)
res = re_telephone.match("13562589631")
print(res)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		