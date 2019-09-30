from pymongo import MongoClient

# 连接服务
coon = MongoClient("localhost",27017)

# 连接数据库
db = coon.mydb

# 获取集合
collection = db.student


collection.remove({"name":"zl"})


# 断开
coon.close()

