
# 元组不能被修改
tuple_demo = ('zhangsan','a','lisi',1,2,1)
print(type(tuple_demo))
print(tuple_demo)

single_tuple = (5)
print(type(single_tuple))

single_tuple = (5,)  # 单元素元组
print(type(single_tuple))

print(tuple_demo[0])  # 元组取值
print(tuple_demo.index('a'))  # 获取元组的元素索引
print(tuple_demo.count(1))  # 统计元素出现次数


print(len(tuple_demo))  # 统计元组元素个数

# 遍历元组
for x in tuple_demo :
	print(x)

# 将元组转换为列表
list_demo = list(tuple_demo)
print(type(list_demo))

# 将列表转换为元组
tuple_demo = tuple(list_demo)
print(type(tuple_demo))


