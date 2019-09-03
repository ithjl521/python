class Father(object):
	def __init__(self,money):
		self.money = money


	def play(self):
		print('play')


	def func(self):
		print('eat')



class Monther(object):
	def __init__(self,faceValue):
		self.faceValue = faceValue


	def play(self):
		print('play')


	def func(self):
		print('run')





class Child(Father,Monther):
	def __init__(self,money,faceValue):
		Father.__init__(self,money)
		Monther.__init__(self,faceValue)




def main():
	c = Child(300,100)
	print(c.money,c.faceValue)
	c.play()
	c.func()  # 父类方法名相同，默认调用前面的


if __name__ == '__main__':
	main()

