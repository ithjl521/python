import tornado.web
from views import index
import config

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/",index.IndexHandler),
			
			(r"/home",index.HomeHandler),
			
			(r"/chat",index.ChatHandler),
		]
		super().__init__(handlers,**config.settings)