name_list = ['zhangsan','lisi','wangwu']

print(name_list)


print(name_list[0])  # 获取下标为0的列表元素

print(name_list.index('lisi'))  # 获取某个元素的索引

name_list[1] = '李四'

name_list.append('zhaoliu')  # 添加一个1元素到列表末尾

name_list.insert(1,'中间')  # 插入一个元素到列表指定索引位置

tmp_list = [1,2,3]

name_list.extend(tmp_list)  # 将一个列表拼接到另外一个列表后面

name_list.remove('zhaoliu')  # 删除列表的某个元素

name_list.pop()  # 删除列表最后一个元素

name_list.pop(3)  # 删除列表指定索引元素

name_list.clear()  # 清空列表

print(name_list)

del name_list  #从内存中删除

list_demo = ['a','b','c'];

print(len(list_demo))  # 列表长度

print(list_demo.count('a'))  # 出现次数

list_sort = [23,12,22,44,11]
list_sort.sort()  # 列表排序
print(list_sort)

list_reverse = ['a','aa','aaa','b','bb']
list_reverse.reverse()  # 列表反转
print(list_reverse)




