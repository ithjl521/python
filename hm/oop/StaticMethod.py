class StaticMethod(object):

	@staticmethod
	def staticmethod():
		print('wo shi jing tai fang fa')


	def a():
		print('putongfangfa')



StaticMethod.staticmethod()
abc = StaticMethod()
abc.staticmethod()
StaticMethod.a()