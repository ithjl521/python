from Person import Person

class Student(Person):

	def __init__(self,name,age,stu_id):
		super().__init__(name,age)
		self.stu_id = stu_id

	def info(self):
		print("%s年龄：%d"%(self.name,self.age))


worker = Student('hjl',23,100)
worker.eat()
worker.info()
print(worker.stu_id)