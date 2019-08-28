class Single(object):
	"""docstring for Single"""
	instance = None

	init_flag = False

	def __new__(cls,*agrs,**kwargs):

		if cls.instance is None:
			cls.instance = super().__new__(cls)

		return cls.instance	


	def __init__(self):

		if Single.init_flag:
			return

		Single.init_flag = True


		