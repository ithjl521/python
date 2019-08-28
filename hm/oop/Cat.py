class Cat:

	def __init__(self,name='tom'):
		print('初始化')
		self.name = name
		self.age = 18


	def __str__(self):
		return 'string'


	def eat(self):
		print('吃鱼')


	def drink(self):
		print('喝水')


	def __del__(self):
		print('销毁')



tom = Cat('bob')
tom.eat()
tom.drink()
print(tom)








