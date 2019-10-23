from flask import Flask
from flask_script import Manager
from views import blue
from views import blue2
import flask
from flask_session import Session
from flask_bootstrap import Bootstrap

app  = Flask(__name__)

# 添加配置
app.config['SECRET_KEY'] = 'EYNDFTBNRE$%^&Gjw9hag34567890'
app.config['SESSION_TYPE'] = 'redis'


Session(app=app)
Bootstrap(app=app)

# 注册蓝图
app.register_blueprint(blueprint=blue)
app.register_blueprint(blueprint=blue2)

manager = Manager(app=app)


if __name__ == '__main__':
	manager.run()