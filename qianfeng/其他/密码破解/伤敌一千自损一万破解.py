#coding=utf8

import itertools

# mylist = list(itertools.product("0123456789qwertyuiopasdfghjklzxcvbnm",repeat=10))

passwd = ("".join(x) for x in itertools.product("0123456789",repeat=3))


while True:
	try:
		str = next(passwd)
		print(str)
	except StopIteration as e:
		break
	