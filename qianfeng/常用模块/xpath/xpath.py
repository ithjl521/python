from lxml import etree

# 生成对象
tree = etree.parse('xpath.html')

# print(tree)
ret = tree.xpath('//div[@class="tang"]/ul/li[1]/text()')
print(ret)

ret2 = tree.xpath('//div[@class="song"]/text()')
ret3 = tree.xpath('//div[@class="song"]//text()')
print(ret3)



