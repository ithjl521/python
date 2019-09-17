from card import Card
from user import User
import random


class ATM(object):

	def __init__(self):
		self.allUser = {}

	# 开户
	def createUser(self):
		name = input('请输入姓名：')
		idCard = input('请输入身份证号码：')
		phone = input('请输入电话号码：')
		prestoreMoney = int(input('输入与存储金额：'))

		if prestoreMoney < 0:
			print('预存储金额小于0')
			return -1

		onePasswd = input('设置密码：')
		if not self.checkPassWd(onePasswd):
			print('密码输入错误，开户失败')


		cardId = self.randomCardId()

	

	# 生成卡号
	def randomCardId(self):
		str = '1'
		
		if self.allUser.get(str):
			return str + '1'
		else:
			return str




	# 查询
	def searchUserInfo(self):
		pass

	# 取款
	def getMoney(self):
		pass

	# 存款
	def saveMoney(self):
		pass

	# 转账
	def transferMoney(self):
		pass

	# 修改密码
	def changePassWd(self):
		pass

	# 锁定
	def lockUser(self):
		pass

	# 解锁
	def unLockUser(self):
		pass

    # 补卡
	def newCard(self):
		pass

	# 注销卡号
	def killUser(self):
		pass

	# 密码验证
	def checkPassWd(self,realPassWd):
		for i in range(3):
			tempPassWd = input('请输入密码：')
			if tempPassWd == realPassWd:
				return True

		return False

