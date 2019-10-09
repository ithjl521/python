import urllib.parse

#image_url = 'https://images-na.ssl-images-amazon.com/images/I/71f8lEiCvHL._SL160_.jpg'

url = 'http://www.baidu.com/index.html?name=何胶龙&pwd=123'

# url编码
ret = urllib.parse.quote(url)
print(ret)

# url解码
re = urllib.parse.unquote(ret)
print(re)