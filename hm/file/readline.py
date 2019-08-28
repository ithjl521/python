
file = open('./write.py')

while True:
	txt = file.readline()

	if not txt:
		break

	print(txt)


file.close()

