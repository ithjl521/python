
import time

class Admin(object):

	admin = '1'
	password = '1'

	def printAdminView(self):
		print('********************************************')
		print('*                                          *')
		print('*                                          *')
		print('*                                          *')
		print('*           欢迎登陆银行系统                *')
		print('*                                          *')
		print('*                                          *')
		print('*                                          *')
		print('********************************************')
		



	def systemFunctionView(self):
		print('********************************************')
		print('*                                          *')
		print('*       开户(1)       查询(2)       		  *')
		print('*       取款(3)       存款(4)       		  *')
		print('*       转账(5)       改密(6)       		  *')
		print('*       锁定(7)       解锁(8)       	      *')
		print('*       补卡(9)       销户(0)       		  *')
		print('*       退出(t)       				      *')
		print('*                                          *')
		print('*                                          *')
		print('********************************************')



	def adminOperate(self):
		inputAdmin = input('请输入管理员账号：')

		if self.admin != inputAdmin:
			print('账号有误！')
			return -1

		inputPass = input('请输入管理员密码：')		
		if self.password != inputPass:
			print('密码有误！')
			return -1

		# 账号密码正确
		print('登陆成功，请稍后')
		time.sleep(2)
		return 0

	

