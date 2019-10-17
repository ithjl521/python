import json
import tornado.web
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
	# 在http方法之前调用
	def initialize(self,param1,param2):
		self.param1 = param1
		self.param2 = param2
	
	def get(self,*args,**kwargs):
		print(self.param1,self.param2)
		self.write('hello tornado')
		
		
# 手动将字典转换成Json字符串（返回的Content-Type是字符串格式）			
class JsonHandler(RequestHandler):
	def get(self,*args,**kwargs):
		per = {
			'name':'hjl',
			'age':18,
			'sex':'男'
		}
		jsonStr = json.dumps(per)
		
		self.write(jsonStr)
		

# 自动将字典转换成Json字符串（write自动转换，返回的Content-Type是json格式）		
class JsonHandler2(RequestHandler):
	def get(self,*args,**kwargs):
		per = {
			'name':'hjl',
			'age':18,
			'sex':'男'
		}
		
		self.write(per)