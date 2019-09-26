import pymysql

# 链接数据库
db = pymysql.connect('127.0.0.1','root','root','python_qianfeng')

# 创建一个cursor对象
cursor = db.cursor()

sql = "select * from student"

# 执行sql语句
cursor.execute(sql)

# 获取返回信息
data = cursor.fetchone()
print(data)

# 断开
cursor.close()
db.close()

