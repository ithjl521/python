src = open('./file.txt')

file_write = open('file_write.txt','w')

while True:

	txt = src.readline()

	if not txt:
		print('复制完成')
		break

	file_write.write(txt)




src.close()
file_write.close()




