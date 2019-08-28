class Person(object):

	def __init__(self,name,age):
		self.name = name
		self.age = age


	def run(self):
		print("%s跑"%(self.name))


	def eat(self):
		print("%s吃"%(self.name))