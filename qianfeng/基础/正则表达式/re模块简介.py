#coding=gbk

import re

'''
re.match���� match(pattern,string,flags=0)
patter��ƥ���������ʽ
string��Ҫƥ����ַ���
flags:��־λ�����ڿ���������ʽ��ƥ�䷽ʽ
	re.I ���Դ�Сд
	re.L �����ػ�ʶ��
	re.M ����ƥ�䣬Ӱ��^��$
	re.S ʹ.ƥ�任�з����ڵ������ַ�
	re.U ����Unicode�ַ��������ַ���Ӱ��\w \W \b \B
	re.X ʹ�����Ը����ĸ�ʽ�������
���ܣ����Դ��ַ�������ʼλ��ƥ��һ��ģʽ�����������ʼλ��ƥ��ɹ��Ļ�������None
ɨ�������ַ��������ش���ʼλ�óɹ���ƥ��
'''

print(re.match('www','www.baidu.com'))
print(re.match('www','ww.baidu.com'))
print(re.match('www','Www.baidu.com',flags=re.I))
print('-'*50)


'''
re.search()
patter��ƥ���������ʽ
string��Ҫƥ����ַ���
flags:��־λ�����ڿ���������ʽ��ƥ�䷽ʽ
���ܣ�ɨ�������ַ����������ص�һ���ɹ���ƥ��
'''

print(re.search('www','abc.baidu.www'))
print('-'*50)


'''
re.findall()
patter��ƥ���������ʽ
string��Ҫƥ����ַ���
flags:��־λ�����ڿ���������ʽ��ƥ�䷽ʽ
���ܣ�ɨ�������ַ����������ؽ���б�
'''

print(re.findall('www','abc.baidu.wwwaga.www'))


