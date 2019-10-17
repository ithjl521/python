import tornado.web
import tornado.ioloop

# 引入httpserver模块
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
	
	def get(self,*args,**kwargs):
		
		self.write('hello tornado')
	

if __name__ == "__main__":
	
	app = tornado.web.Application([
		(r"/",IndexHandler)
	])
	
	#app.listen(8000)
	# 实例化一个http服务器对象
	httpServer = tornado.httpserver.HTTPServer(app)

	# httpServer.listen(8000)
	httpServer.bind(8000)  # 将服务器绑定到指定端口
	httpServer.start(5)  # 5代表启动5个进程，默认是1，如果写负数、0或者None则会开启硬件对应核心数个进程
	
	# 因为一些问题，不建议这样启动多个进程。我们建议手动启动多个进程，并且绑定不同的端口
	# 原因：①每个子进程都会从父进程中复制一份IOLoop的实例，如果再创建子进程前修改了IOLoop，会影响所有子进程
	#		②所有的进程都是由一个命令启动的，无法做到在不停止服务的情况下，修改代码
	#		③所有进程共享一个端口，想要分别监控很困难
	
	tornado.ioloop.IOLoop.current().start()
