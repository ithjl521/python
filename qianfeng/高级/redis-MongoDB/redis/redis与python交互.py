import redis

# 连接
r = redis.Redis(host="localhost",port=6379)


# 1、根据数据类型不同，调用相应的方法
# 写
r.set('p1','good')

# 读
print(r.get('p1'))


# 2、pipline 缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set("p2","nice")
pipe.set("p3","nice3")
pipe.set("p4","nice4")
pipe.execute()

print(r.get('p2'))






