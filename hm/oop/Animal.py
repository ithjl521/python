class Animal:
	def eat(self):
		print('吃')


	def drink(self):
		print('喝')


	def run(self):
		print('跑')


	def sleep(self):
		print('睡')




class Dog(Animal):
	"""docstring for Dog"""
	def bark(self):
		print('叫')



class XiaoTianQuan(Dog):
	"""docstring for XiaoTianQuan"""
	def fly(self):
		print('飞')

	def bark(self):
		print('咆哮')
		super().bark()
		print('((((((')

	def run(self):
		print('天上跑')

		
	
class Cat(object):
		"""docstring for Cat"""
		def catch(self):
			print('抓老鼠')
				

		

xiaotianquan = XiaoTianQuan()

xiaotianquan.bark()




