#coding=gbk

import urllib.request

# ��ָ����url��ַ�������󣬲����ط�������Ӧ�����ݣ��ļ��Ķ���
response = urllib.request.urlopen("https://www.baidu.com")

# ��ȡ�ļ���ȫ�����ݣ���Ѷ�ȡ�������ݸ�ֵ��һ���ַ�������
# data = response.read().decode('utf-8')

# ��ȡһ��
# data = response.readline()

# ��ȡ�ļ���ȫ�����ݣ���Ѷ�ȡ�������ݸ�ֵ��һ���б����
# data = response.readlines()
# print(type(data))


# ����ȡ������ҳд���ļ�
# with open(r"C:\Users\jiuzhou\Desktop\python\qianfeng\�߼�\����\file\file1.html",'w') as f:
	# f.write(data)
	
# response ����
# ���ص�ǰ�������й���Ϣ
# print(response.info())

# ����״̬��
# print(response.getcode())

# ���ص�ǰ������ȡ��url��ַ
# print(response.geturl())





