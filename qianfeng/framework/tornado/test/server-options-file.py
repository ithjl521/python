import tornado.web
import tornado.ioloop
import tornado.options

# 引入httpserver模块
import tornado.httpserver

'''
name:变量名，不能重复
default：默认值，不设置默认为None
type：设置变量类型，从命令行或者配置文件导入参数时，tornado会根据类型转换输入的值，转换不成会报错，可以是str、float、int、datetime、timestamp
	  如果没有设置type，会根据default的值进行转换。如果default没有设置，不进行转换
multiple：设置选项变量是否可以为多个值，默认为False
help：选项变量的帮助提示信息
'''
tornado.options.define(name='port',default=None,type=None,multiple=False,help=None)
tornado.options.define(name='list',default=[],type=str,multiple=True)


class IndexHandler(tornado.web.RequestHandler):
	
	def get(self,*args,**kwargs):
		
		self.write('hello tornado')
	

if __name__ == "__main__":

	# 转换配置文件转换参数
	tornado.options.parse_config_file("config.conf")
	
	app = tornado.web.Application([
		(r"/",IndexHandler)
	])
	
	#app.listen(8000)
	# 实例化一个http服务器对象
	httpServer = tornado.httpserver.HTTPServer(app)

	# httpServer.listen(8000)
	
	# 定义的变量都是该对象的属性
	# tornado.options.options
	httpServer.bind(tornado.options.options.port)  # 将服务器绑定到指定端口
	httpServer.start()  
	
	
	tornado.ioloop.IOLoop.current().start()
