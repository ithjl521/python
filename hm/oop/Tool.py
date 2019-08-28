class Tool(object):

	count = 0

	def __init__(self,name):
		self.name = name
		Tool.count += 1
		# self.count += 1


tool1= Tool('futou')
tool2= Tool('maoie')
tool3= Tool('fuzi')

Tool.count = 99
print(Tool.count)
