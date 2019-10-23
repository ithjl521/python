from flask import Blueprint
import flask

# 定义蓝图
blue = Blueprint('first_blue',__name__)
blue2 = Blueprint('seconde_blue',__name__)

# 使用蓝图定义路由
@blue.route('/hello')
@blue.route('/hi')
def hello():
	return flask.render_template('hello.html')
	
@blue2.route('/urlfor')
def url():
	result = flask.url_for('seconde_blue.index')
	return result
	
@blue2.route('/index')
def index():
	return flask.render_template('index.html')

@blue2.route('/mine')
def mine():
	return flask.render_template('mine.html')
		

@blue2.route('/hellobs')
def hello_bs():
	return flask.render_template('hello_bootstrap.html')
		
	
@blue.route('/home')
def home():
	username = flask.request.cookies.get('user')
	return flask.render_template('home.html',username=username)
	
@blue.route('/login',methods=['GET','POST'])
def login():
	if flask.request.method == 'GET':
	
		return flask.render_template('login.html')
	else:
		username = flask.request.form.get('username')
		resp = flask.Response(response='登陆成功%s'% username)
		resp.set_cookie('user',username)
		
		return resp
		
	
@blue.route('/logout')
def logout():
	resp = flask.redirect(flask.url_for('first_blue.home'))
	resp.delete_cookie('user')
	return resp