from Person import Person

class Worker(Person):

	def __init__(self,name,age):
		super().__init__(name,age)


worker = Worker('hjl',23)
worker.run()

