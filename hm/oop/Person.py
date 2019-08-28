class Person:

	def __init__(self,name,weight):

		self.name = name
		self.weight = weight


	def __str__(self):

		return "我的名字shi%s体重是%.2f公斤"%(self.name,self.weight)


	def eat(self):
		print('吃饭')
		self.weight +=1


	def run(self):
		print('跑步')
		self.weight -=0.5


wo = Person('小明',55)
wo.eat()
wo.run()
print(wo)



