from bs4 import BeautifulSoup

# 生成对象
soup = BeautifulSoup(open('test_soup.html',encoding='utf8'),'lxml')

# print(type(soup))

# 根据标签查找，只能找到第一个符合要求的标签
# print(soup.a)

# 获取标签属性值
# print(soup.a['href'])
# print(soup.a.attrs) # 获取所有属性
# print(soup.a.attrs['title'])

# 获取标签内的内容
# print(soup.div.text)
# print(soup.div.string)  # 如果内容含有标签，则获取结果为None
# print(soup.div.get_text())


# 找到第一个符合要求的a
# print(soup.find('a'))

# 找到title为qing的a标签
# print(soup.find('a',title='qing'))
# 找到class为du的a标签
# print(soup.find('a',class_='du'))


# 可以先找到div，再找到div里面的a标签，多个符合要求的，总是找到第一个
# div = soup.find('div',class_='tang')
# print(div.find('a',class_='du'))

# 找到所以符号要求的标签，返回一个列表
# print(soup.find_all('a'))
# 找到所有的i和b标签
# print(soup.find_all(['i','b']))
# 找到所有a标签，取前两条
# print(soup.find_all('a',limit=2))


# 根据选择器选择指定的内容
# print(soup.select('.tang > ul > li > a')[2])
print(soup.select('#feng')[0]['href'])


