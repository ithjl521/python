class Person(object):


	def __init__(self,name,age):
		self.name = name
		self.__age = age

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self,age):
		if age < 0:
			age = 0

		self.__age = age


per = Person('hjl',23)

per.age = 100
print(per.age)
