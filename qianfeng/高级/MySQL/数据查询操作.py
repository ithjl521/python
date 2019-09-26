import pymysql

# 链接数据库
db = pymysql.connect('127.0.0.1','root','root','python_qianfeng')

# 创建一个cursor对象
cursor = db.cursor()

sql = "select * from student"

# 执行sql语句
cursor.execute(sql)

#获取返回信息
# data = cursor.fetchone()  # 结果集是一个对象,一条数据
# print(data)

data2 = cursor.fetchall()  # 获取全部数据
for row in data2:
	print(row)

# 断开
cursor.close()
db.close()

