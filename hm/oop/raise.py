
def input_password():
	password = input('输入密码：')

	if len(password) < 8:
		ex = Exception('密码长度不够')
		raise ex

	return password



try:
	print(input_password())
except Exception as e:
	print(e)