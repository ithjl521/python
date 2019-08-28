row=1
while row<=9:
	col=1
	while col<=row:
		ji = col * row
		print("%d * %d = %d\t"%(col,row,ji),end='')
		col+=1
		
	print()
	row+=1
	