#coding=utf8

def checkPhone(str):
	if len(str) != '11':
		return False
	elif str[0] != '1':
		return False
	elif str[1:3] != '30' and str[1:3] != '31':
		return False
	for i in range(3,11):
		if str[i] < '0' or str[i] > '9':
			return False
		
	return True
	
	
print(checkPhone('13920366598'))
print(checkPhone('13120366598'))