#coding=gbk

import urllib.request
import os

os.environ['http_proxy'] = ''

urllib.request.urlretrieve("http://www.baidu.com",filename=r"C:\Users\jiuzhou\Desktop\python\qianfeng\�߼�\����\file\file2.html")
# urlretrieve��ִ�й����У������һЩ����
# �������
urllib.request.urlcleanup()
