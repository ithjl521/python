from pymongo import MongoClient

# 连接服务
coon = MongoClient("localhost",27017)

# 连接数据库
db = coon.mydb

# 获取集合
collection = db.student


# 添加文档
# collection.insert({"name":"hjl","age":23,"gender":1,"address":"深圳","isDelete":0})

# 批量添加
collection.insert([
	{"name":"hjl","age":23,"gender":1,"address":"深圳","isDelete":0},
	{"name":"zl","age":24,"gender":0,"address":"成都","isDelete":0}
])


# 断开
coon.close()

