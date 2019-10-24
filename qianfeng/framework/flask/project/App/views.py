
from flask import Blueprint, current_app

from App.ext import db
from App.models import Student
import flask
import random

blue = Blueprint('first_blue',__name__)


def init_blue(app):
	app.register_blueprint(blueprint=blue)


@blue.route("/")
def index():
	return 'hello'
	

@blue.route('/addstu')
def add_stu():
	num = random.randrange(100)

	stu = Student()
	stu.s_name = '小花%d号'% num
	db.session.add(stu)
	db.session.commit()
	
	return 'add success'
	
	
@blue.route('/getstu')
def get_stu():
	# stus = Student.query.filter(Student.id.__gt__(3))
	
	stus = Student.query.filter(Student.id > 10)
	
	return flask.render_template('stus.html', stus=stus)


@blue.route('/configlist')
def config_list():
	print(current_app.config)
	return flask.render_template('config_list.html')