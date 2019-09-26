import pymysql

# 链接数据库
db = pymysql.connect('127.0.0.1','root','root','python_qianfeng')

# 创建一个cursor对象
cursor = db.cursor()


# 检查表是否存在，存在则删除
cursor.execute('drop table if exists abc')

# 创建表
sql = 'create table abc(id int auto_increment primary key,money int not null)'
cursor.execute(sql)

# 断开
cursor.close()
db.close()

