#coding=gbk

import re

'''
�ַ����и�
'''
str1 = "hjl   is a good    man"
print(re.split(r" +",str1))



'''
re.finditer����
ԭ��re.finditer(pattern,string,flags=0)
patter��ƥ���������ʽ
string��Ҫƥ����ַ���
flags:��־λ�����ڿ���������ʽ��ƥ�䷽ʽ
���ܣ���findall���ƣ�ɨ�������ַ���������һ��������
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
�ַ����滻���޸�
re.sub(pattern,repl,string,count=0,flags=0)
re.subn(pattern,repl,string,count=0,flags=0)	
pattern  ������ʽ
repl 	  ָ���������滻���ַ���
string 		Ŀ���ַ���
count=0 	����滻����
flags=0	
���ܣ���Ŀ���ַ�������������ʽ�Ĺ���ƥ���ַ������ٰ������滻��ָ�����ַ�����
	����ָ���滻�Ĵ����������ָ����ȫ���滻
����ǰ�߷��ر��滻�ɵ��ַ�����
	���߷���һ��Ԫ�飬Ԫ���һ��Ԫ���Ǳ��滻�ɵ��ַ������ڶ���Ԫ���Ǳ��滻����
'''
str5 = 'hjl is a good good good man'
print(re.sub(r'(good)','nice',str5))
print(re.subn(r'(good)','nice',str5))		
		
		

'''
���飺
������˼򵥵��ж��Ƿ�ƥ��֮�⣬������ʽ������ȡ���Ӵ��Ĺ��ܣ���()С���ű�ʾ�ľ�����ȡ���顣
'''		
str3 = "010-23458712"
m = re.match(r"((?P<first>\d{3})-(?P<last>\d{8}))",str3)
# ʹ����Ż�ȡ��Ӧ�����Ϣ��group(0)һֱ����ԭʼ�ַ���
print(m.group(0))
print(m.group(1))
print(m.group('first')) # ͨ���Լ�ȡ�������ȡ����
print(m.group(2))

# �鿴ƥ��ĸ�������
print(m.groups())
		
		
		
		
'''
���룺������ʹ��������ʽʱ��reģ�����������
1������������ʽ�����������ʽ�����Ϸ����ᱨ��
2���ñ�����������ʽȥƥ�����
re.compile(pattern,flags=0)
	pattern:Ҫ�����������ʽ
'''	

pat = r"^1(([3578]\d)|(47))\d{8}$"
# ������������	
re_telephone = re.compile(pat)
res = re_telephone.match("13562589631")
print(res)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		