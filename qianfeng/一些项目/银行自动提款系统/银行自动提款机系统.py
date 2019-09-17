from admin import Admin
from atm import ATM

def main():
	

	# 界面对象
	admin = Admin()

	# 开机
	admin.printAdminView()

	# 管理员登录
	if admin.adminOperate():
		return -1

	atm = ATM()


	while True:
		admin.systemFunctionView()

		option = input('请输入你的操作：')

		if option == '1':
			print('开户')
			atm.createUser()
		elif option == '2':
			print('查询')
		elif option == '3':
			print('取款')
		elif option == '4':
			print('存储')
		elif option == '5':
			print('转账')
		elif option == '6':
			print('改密')
		elif option == '7':
			print('锁定')
		elif option == '8':
			print('解锁')
		elif option == '9':
			print('补卡')
		elif option == '0':
			print('销户')
		elif option == 't':
			print('退出')
			if admin.adminOperate():
				return -1


if __name__ == '__main__':
	main()



