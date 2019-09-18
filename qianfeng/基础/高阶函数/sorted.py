# coding=gbk
# 排序


list1 = [2,3,41,5,0,1]
list2 = sorted(list1)
print(list1)
print(list2)

# 绝对值的大小排序
list3 = [-2,-1,1,34,5,-10]
# key接收函数来实现自定义排序
list4 = sorted(list3,key=abs)
print(list3)
print(list4)


# 降序
list5 = [2,3,41,5,0,1]
# reverse 是否反转
list6 = sorted(list5,reverse=True)
print(list5)
print(list6)

