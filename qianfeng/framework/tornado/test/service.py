import tornado.web
'''
tornado.web：tornado的基础web框架模块
'''

import tornado.ioloop
'''
tornado.ioloop tornado的核心IO循环模块
封装了linux的epoll和BSD的kqueue，是tornado高效的基础
'''

# 业务处理类
class IndexHandler(tornado.web.RequestHandler):
	# 重写get方法，处理get请求
	def get(self,*args,**kwargs):
		# 对应http请求的方法，给浏览器响应信息
		self.write('hello tornado')
	

if __name__ == "__main__":
	# 实例化一个App对象
	# Application：是tornado web框架的核心应用类，是与服务器对应的接口
	# 里面保存了路由映射表，该类有一个listen方法用来创建一个http服务器实例，并绑定端口
	app = tornado.web.Application([
		(r"/",IndexHandler)
	])
	
	# 绑定监听端口
	# 注意：此时服务器并没有开启监听
	app.listen(8000)  # 只能在单进程模式中使用
	
	'''
	IOLoop.current()：返回当前线程的IOLoop实例
	IOLoop.srart()：启动IOLoop实例的I/O循环，同时开启了监听
	'''
	tornado.ioloop.IOLoop.current().start()
