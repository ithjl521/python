#coding=gbk

import urllib.request
import urllib.parse

url = "http://www.test.com"

# ��Ҫ���͵����ݺϳ�һ���ֵ�
# �ֵ�ļ�ȥ��ַ���ң�һ��Ϊinput��ǩ��name����ֵ
data = {
	"username":"hjl"
	"password":"admin123"
}

# ��Ҫ���͵����ݽ��д��(�������Ҫ)
postData = urllib.parse.urlencode(data).encode("utf-8")

# ������
req = urllib.request.Request(url,data=postData)
#����
req.add_header("User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")

response = urllib.request.urlopen(req)

print(response.read())

