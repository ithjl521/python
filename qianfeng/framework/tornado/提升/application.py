import tornado.web
from views import index
import config
import os

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			# 传参数的路由
			# (r"/",index.IndexHandler,{'param1':'good','param2':'nice'}),
			
			(r'/json',index.JsonHandler),
			
			(r'/json2',index.JsonHandler2),
			
			# 响应头
			(r'/header',index.HeaderHandler),
			
			# 状态码
			(r'/status',index.StatusCodeHandler),
			
			# 重定向
			(r'/index',index.RedirectHandler),
			
			# 错误处理
			(r'/iserror',index.ErrorHandler),
			
			# 另外一种路由方式
			tornado.web.url(r'/longge',index.LongHandler,
			{'param1':'good','param2':'nice'},name='longge'),
			
			# 截取地址栏URI传参(正则匹配)
			(r'/liuyifei/(\w+)/(\w+)/(\w+)',index.LiuYiFeiHandler),
			
			# get传参
			(r'/get_params',index.GetParamsHandler),
			
			# post传参
			(r'/post_params',index.PostParamsHandler),
			
			# request对象
			(r'/request_demo',index.RequestDemoHandler),
			
			 # 模板
			 (r'/template',index.TemplateHandler),
			 
			 # 数据库
			 (r'/sql_test',index.SqlTestHandler),
			 
			 # 普通cookie
			 (r'/p_cookie',index.PCookieHandler),
			 
			 # 安全cookie
			 (r'/s_cookie',index.SCookieHandler),
			 
			 
			 
			 # 静态路由，要放在所有路由最下面
			 (r'/(.*)$',tornado.web.StaticFileHandler,
			 {'path':os.path.join(config.BASE_DIRS,'static/html'),'default_filename':'index.html'}),
		]
		super().__init__(handlers,**config.settings)
		
		
		
		
		