from flask import Blueprint

blue = Blueprint('first_blue',__name__)

@blue.route('/hello')
def hello():
	return 'hello'