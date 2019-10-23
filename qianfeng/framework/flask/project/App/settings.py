

def get_db_uri(dbinfo):
	ENGINE = dbinfo.get('ENGINE')
	DRIVER = dbinfo.get('DRIVER')
	USER = dbinfo.get('USER')
	PASSWORD = dbinfo.get('PASSWORD')
	HOST = dbinfo.get('HOST')
	PORT = dbinfo.get('PORT')
	NAME = dbinfo.get('NAME')
	
	return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE,DRIVER,USER,PASSWORD,HOST,PORT,NAME)

class Config:
	DEBUG = False
	TESTING = False
	SECRET_KEY = '$%^&*(NKJHUDGMKHYTTYrthjk34567u8fghji456uifghj456'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	
class DevelopConfig(Config):
	DEBUG = True
	
	DATABASE = {
		'ENGINE':'mysql',
		'DRIVER':'pymysql',
		'USER':'root',
		'PASSWORD':'root',
		'HOST':'localhost',
		'PORT':'3306',
		'NAME':'test'		
	}
	
	SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

	
class TestingConfig(Config):
	TESTING = True
	
	DATABASE = {
		'ENGINE':'mysql',
		'DRIVER':'pymysql',
		'USER':'root',
		'PASSWORD':'root',
		'HOST':'localhost',
		'PORT':'3306',
		'NAME':'test'		
	}
	
	SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
	
	
class StagingConfig(Config):
	
	DATABASE = {
		'ENGINE':'mysql',
		'DRIVER':'pymysql',
		'USER':'root',
		'PASSWORD':'root',
		'HOST':'localhost',
		'PORT':'3306',
		'NAME':'test'		
	}
	
	SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

	
class ProductConfig(Config):
	
	DATABASE = {
		'ENGINE':'mysql',
		'DRIVER':'pymysql',
		'USER':'root',
		'PASSWORD':'root',
		'HOST':'localhost',
		'PORT':'3306',
		'NAME':'test'		
	}
	
	SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)		
	

envs = {
	'develop':DevelopConfig,
	'testing':TestingConfig,
	'staging':StagingConfig,
	'product':ProductConfig
}
	
	
	
	
	
	
	
	
	
	