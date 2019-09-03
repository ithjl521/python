from types import MethodType

class Person(object):

	def __init__(self,name):
		self.name = name

	def eat(self):
		print('eat')


def say(self):
	print('hello')


hjl = Person('hjl')
hjl.say = MethodType(say,hjl)

hjl.say()



