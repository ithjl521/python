#coding=utf8

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

'''


res = re.match(��www','www.baidu.com')
print(res)
