import urllib.parse

url = 'http://www.baidu.com/index.html'

data = {
	'name':'孤胆',
	'age':18,
	'sex':'nv',
	'height':180
}

# 拼接url
'''
lt = []

for k,v in data.items():
	lt.append(k + '=' + str(v))
	
query_string = '&'.join(lt)

url = url + '?' + query_string

print(url)
'''

# 参数是一个字典，将字典拼接为query_string，并且已经编码
query_string = urllib.parse.urlencode(data)
print(query_string)
