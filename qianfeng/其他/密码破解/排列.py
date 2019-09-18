#coding=gbk

import itertools

mylist = list(itertools.permutations([1,2,3,4],3))
print(mylist)


'''
4->3  24
4->2  12
4->1  1

排列的可能性次数：
n! / (n-m)!

'''




