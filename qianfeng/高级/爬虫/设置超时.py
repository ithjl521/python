#coding=gbk
import urllib.request
import os

# �����ҳ��ʱ��δ��Ӧ��ϵͳ�ж���ʱ���޷���ȡ
for i in range(1,100):
	try:
		response = urllib.request.urlopen("http://www.baidu.com",timeout=0.5)
	except:
		print("����ʱ")
