def sum1(n):
	if n == 1:
		return 1
	else:
		return n + sum1(n-1)


print(sum1(5))

