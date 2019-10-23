from flask import Flask
from App.ext import init_ext
from App.views import init_blue
from App.settings import envs

def create_app():
	app = Flask(__name__)
	
	# 初始化配置
	app.config.from_object(envs.get('develop'))
	
	# 注册蓝图，初始化
	init_blue(app)
	
	
	
	# 初始化第三方库
	init_ext(app)
	
	return app