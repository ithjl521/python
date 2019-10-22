from flask import Flask
from flask_script import Manager
import flask



app = Flask(__name__)
mananer = Manager(app=app)

@app.route('/')
def index():
	return 'hello flask script'

@app.route('/hello/')
def hello():
	return flask.render_template('hello.html')

@app.route('/params/<kw1>/<string:name>')
def params(kw1,name):
	print(type(kw1))
	print(kw1)
	return '获取参数'+kw1+name

@app.route('/any/<any(c,d,e):an>',methods=['GET','POST'])
def any(an):
	print(an)
	print(type(an))
	return 'any'

@app.route('/url')
def url():
	res = flask.url_for('hello')
	print(res)
	print(flask.url_for('any',an='d'))
	return '反向解析'


@app.route('/request',methods=['GET','POST'])
def req():
	'''
	print(flask.request)
	print(flask.request.method)
	print(flask.request.data)
	print(flask.request.args)  # get请求数据
	print(flask.request.form)  # post相关数据
	print(flask.request.files)
	print(flask.request.cookies)
	print(flask.request.remote_addr)
	print(flask.request.url)
	'''
	print(flask.request.args.get('user'))
	print(flask.request.args.getlist('user'))

	return '请求'


@app.route('/response')
def resp():
	res = flask.render_template('hello.html')
	# print(res)

	# response = flask.make_response('<h2>哈哈</h2>')
	response = flask.Response(response='自己造的response',status=403)

	return response

	# return '<h2>响应</h2>',401	# 第二个参数返回状态码

@app.route('/redirect')
def redir():
	return flask.redirect(flask.url_for('hello'))


@app.route('/abort')
def ab():
	flask.abort(405)  # 禁止


@app.route('/json')
def json_test():
	# return flask.json.jsonify({'name':'hjl'})
	# return flask.json.jsonify(name='hjl',age=18)
	return flask.json.dumps({'name':'hjl'})



if __name__ == '__main__':
	# app.run(debug=True,port=8000,host='0.0.0.0')
	mananer.run()


