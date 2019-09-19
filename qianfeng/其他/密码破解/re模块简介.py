#coding=utf8

import re

'''
re.match函数 match(pattern,string,flags=0)
patter：匹配的正则表达式
string：要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
	re.I 忽略大小写
	re.L 做本地化识别
	re.M 多行匹配，影响^和$
	re.S 使.匹配换行符在内的所有字符
	re.U 根据Unicode字符集解析字符，影响\w \W \b \B
	re.X 使我们以更灵活的格式理解正则
功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，返回None

'''


res = re.match(’www','www.baidu.com')
print(res)
