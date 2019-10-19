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
		# 反向解析，获取name为longge的对应路由
		url = self.reverse_url('longge')
		self.write("<a href='%s'>去另外一个页面</a>"%(url))
		
		
# 手动将字典转换成Json字符串（返回的Content-Type是字符串格式）			
class JsonHandler(RequestHandler):
	def get(self,*args,**kwargs):
		per = {
			'name':'hjl',
			'age':18,
			'sex':'男'
		}
		jsonStr = json.dumps(per)
		
		# 可以设置响应头
		self.set_header('Content-type','application/json;charset=UTF-8')
		
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
		
		
class HeaderHandler(RequestHandler):
	# 在进入http响应处理方法之前被调用，可以重写该方法来预先设置默认headers
	def set_default_headers(self):
		self.set_header('Content-type','text/html;charset=UTF-8')

	def get(self,*args,**kwargs):
		per = {
			'name':'hjl',
			'age':18,
			'sex':'男'
		}
		
		self.write(per)
		

class StatusCodeHandler(RequestHandler):
	
	def get(self,*args,**kwargs):
		# 设置返回状态码
		# self.set_status(404)
		self.set_status(999,'who am I?')
		self.write('*'*50)
		
		
class RedirectHandler(RequestHandler):
	
	def get(self,*args,**kwargs):
		# 重定向
		self.redirect('/')
		
		
class ErrorHandler(RequestHandler):

	def write_error(self,status_code,**kwargs):
		if status_code == 500:
			self.set_status(500)
			self.write('服务器错误')
		elif status_code == 404:
			self.set_status(404)
			self.write('找不到')
		else:
			self.set_status(999)
			self.write('未知错误')
	
	def get(self,*args,**kwargs):
		# 获取参数
		flag = self.get_query_argument('flag')
		
		if flag == '0':
			# 抛出错误，执行write_error()方法
			self.send_error(500)
		
		self.write('you are write')
		
		
class LongHandler(RequestHandler):
	def initialize(self,param1,param2):
		self.param1 = param1
		self.param2 = param2
	
	
	def get(self,*args,**kwargs):
		
		self.write('hjl is a good man\n')
		
		self.write(self.param1+'\n')
		
		self.write(self.param2)
		

class LiuYiFeiHandler(RequestHandler):
	
	def get(self,h1,h2,h3,*args,**kwargs):
		print(h1+'-'+h2+'-'+h3)	
		self.write('liuyifei')
		

class GetParamsHandler(RequestHandler):
	
	def get(self,*args,**kwargs):
		# name 指定参数名，如果有多个同名参数，返回最后一个
		# default 设置未传递的name参数时返回的默认值，如果default没有设置，会抛出异常
		# strip 表示过滤参数值两边的空白字符
		# http://192.168.88.244:8080/get_params?a=1&b=2&c=3
		a = self.get_query_argument(name='a',default=0,strip=True)
		b = self.get_query_argument(name='b',default=0,strip=True)
		c = self.get_query_argument(name='c',default=0,strip=True)
		self.write('get方式传参')
		print(a,b,c)
		
		
class PostParamsHandler(RequestHandler):
	
	def get(self,*args,**kwargs):
		# 渲染页面
		self.render('postfile.html')

	def post(self,*args,**kwargs):
		# 接收post参数
		name = self.get_body_argument(name='username',default='a',strip=True)
		password = self.get_body_argument(name='password',default='123',strip=True)
		hobbyList = self.get_body_arguments(name='hobby')
		print(name,password,hobbyList)
		

class RequestDemoHandler(RequestHandler):
	
	def get(self,*args,**kwargs):
		print(self.request.method)
		print(self.request.host)
		print(self.request.uri)
		print(self.request.query)
		print(self.request.version)
		print(self.request.headers)
		print(self.request.body)
		print(self.request.remote_ip)
		print(self.request.files)
		
		self.write("requestHandler 对象")
		

class TemplateHandler(RequestHandler):
	def get(self,*args,**kwargs):
		temp = 100
		
		per = {
			'name':'hjl',
			'age':'18'
		}
		
		stus = [
			{'name':'hjl','age':23},
			{'name':'dalao','age':99}
		]
		
		# 函数也可以传递
		def mySum(n1,n2):
			return n1+n2
		
		# 渲染模板，传递参数
		self.render('home.html',num=temp,per=per,**per,stus=stus,mySum=mySum)
		
class SqlTestHandler(RequestHandler):
	def get(self,*args,**kwargs):
		self.render('sql_test.html')
		print(self.application)
		
		
		
		
		