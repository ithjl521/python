import tornado.web
from views import index
import config

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/",index.IndexHandler,{'param1':'good','param2':'nice'}),
			
			(r'/json',index.JsonHandler),
			
			(r'/json2',index.JsonHandler2),
			
			
		]
		super().__init__(handlers,**config.settings)