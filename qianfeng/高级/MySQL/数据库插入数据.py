import pymysql

# 链接数据库
db = pymysql.connect('127.0.0.1','root','root','python_qianfeng')

# 创建一个cursor对象
cursor = db.cursor()



sql = 'insert into abc values(0,1)'
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

# 断开
cursor.close()
db.close()

