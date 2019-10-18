import tornado.web
from views import index
import config

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			# ��������·��
			(r"/",index.IndexHandler,{'param1':'good','param2':'nice'}),
			
			(r'/json',index.JsonHandler),
			
			(r'/json2',index.JsonHandler2),
			
			# ��Ӧͷ
			(r'/header',index.HeaderHandler),
			
			# ״̬��
			(r'/status',index.StatusCodeHandler),
			
			# �ض���
			(r'/index',index.RedirectHandler),
			
			# ������
			(r'/iserror',index.ErrorHandler),
			
			# ����һ��·�ɷ�ʽ
			tornado.web.url(r'/longge',index.LongHandler,
			{'param1':'good','param2':'nice'},name='longge'),
			
			# ��ȡ��ַ��URI����(����ƥ��)
			(r'/liuyifei/(\w+)/(\w+)/(\w+)',index.LiuYiFeiHandler),
			
			# get����
			(r'/get_params',index.GetParamsHandler),
			
			# post����
			(r'/post_params',index.PostParamsHandler),
			
			# request����
			(r'/request_demo',index.RequestDemoHandler),
			
			 # ģ��
			 (r'/template',index.TemplateHandler),
		]
		super().__init__(handlers,**config.settings)