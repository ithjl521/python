from Person import Person

class Man(Person):
	"""docstring for Man"""
	def __init__(self,name,age):
		super().__init__(name,age)

	def eat(self):
		print('%s狂吃'%self.name)
		

man = Man('hjl',23)
man.eat()