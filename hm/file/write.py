file = open('./file.txt','w')


file.write('hello')

try:
	txt = file.read()
except Exception as e:
	
	print('error')


file.close()

