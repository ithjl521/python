import tornado.web
import tornado.ioloop
import config
import tornado.httpserver

from application import Application
	

if __name__ == "__main__":
	app = Application()
	
	httpServer = tornado.httpserver.HTTPServer(app)
	httpServer.bind(config.options['port'])  
	httpServer.start()  
	
	tornado.ioloop.IOLoop.current().start()
