#coding=gbk

import itertools

mylist = list(itertools.combinations([1,2,3,4,5],4))
print(mylist)

'''
m  n
5->5 1
5->4 5
5->3 10
5->2 10
m! / (n! * (m-n)!)
'''

