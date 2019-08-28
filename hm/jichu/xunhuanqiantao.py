# i = 0;
# while i < 5:
# 	str = '*' * (i+1)
# 	print(str)
# 	i+=1

row = 1
while row<=5:
	i = 1
	while i<=row:
		print('*',end="")
		i+=1
	print('')  # 换行
	row+=1