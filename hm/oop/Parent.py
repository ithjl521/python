class ParentA:
	def __init__(self,num1):
		self.num1 = num1

	def test(self):
		print('testa')


	def demo(self):
		print('demoa')



class ParentB:

	def demo(self):
		print('demob')

	def test(self):
		print('testb')






class Child(ParentB,ParentA):
	pass



child = Child(1)
child.demo()
child.test()
print(Child.__mro__)  # 查看方法搜索顺序
print(dir(child))  # 查看对象有哪些属性和方法




