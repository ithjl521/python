from flask import Flask
from flask_script import Manager


app = Flask(__name__)
mananer = Manager(app=app)

@app.route('/')
def index():
	return 'hello flask script'
	
if __name__ == '__main__':
	# app.run(debug=True,port=8000,host='0.0.0.0')
	mananer.run()
