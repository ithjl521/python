import tornado.web
import tornado.ioloop
import config

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
	httpServer.bind(config.options['port'])  # 将服务器绑定到指定端口
	httpServer.start()  
	
	
	tornado.ioloop.IOLoop.current().start()
