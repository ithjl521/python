
import tornado.web
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler

class IndexHandler(RequestHandler):
	
	def get(self,*args,**kwargs):
		
		self.write('hello tornado')
		
		
class HomeHandler(RequestHandler):
	def get(self,*args,**kwargs):
		
		self.render('home.html')
		
class ChatHandler(WebSocketHandler):
	users = []
	
	# 客户端websocket连接后调用
	def open(self):
		# 将所有连接加入到users列表
		self.users.append(self)
		# 给每个连接客户端返回消息
		for user in self.users:
			user.write_message(u"[%s登录了]"%(self.request.remote_ip))
			
	# 客户端连接关闭后调用	
	def on_close(self):
		# 当客户端关闭时候，发送消息给所有用户，不给当前用户发送，所以先删除当前用户
		self.users.remove(self)
		for user in self.users:
			user.write_message(u"[%s退出了]"%(self.request.remote_ip))
		
	# 客户端发送消息调用
	def on_message(self,message):
		for user in self.users:
			user.write_message(u"[%s]说：%s"%(self.request.remote_ip,message))
		
	# def check_origin(self,origin):
		# return True
