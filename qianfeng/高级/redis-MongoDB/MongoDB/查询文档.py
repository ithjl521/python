import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId  # 用于ID查询

# 连接服务
coon = MongoClient("localhost",27017)

# 连接数据库
db = coon.mydb

# 获取集合
collection = db.student


# 查询部分文档、排序、分页
res = collection.find({"age":{"$gt":18}}).sort("age",pymongo.DESCENDING).skip(1).limit(2)

# 查询所有文档
# res = collection.find()

for row in res:
	print(row)
	print(type(row))

# 统计查询
count = collection.find({"age":{"$gt":18}}).count()
print(count)

# 根据ID查询
one_record = collection.find({"_id":ObjectId("5d915cbf05ffcdc79c6aa05c")})
print(one_record)


# 断开
coon.close()

