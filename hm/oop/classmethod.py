class ClassMethod(object):

	count = 0

	@classmethod
	def abc(cls):
		print('我是类方法')
		print(cls.count)



ClassMethod.abc()