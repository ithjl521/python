
from flask import Blueprint
from App.ext import db
from App.models import Student

blue = Blueprint('first_blue',__name__)

def init_blue(app):
	app.register_blueprint(blueprint=blue)

@blue.route("/")
def index():
	return 'hello'
	

@blue.route('/addstu')
def add_stu():
	stu = Student()
	stu.s_name = '小花'
	db.session.add(stu)
	db.session.commit()
	
	return 'add success'
	