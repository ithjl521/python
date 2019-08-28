import time

# 返回当前时间时间戳，浮点数形式
c = time.time()
print(c)

# 将时间戳转换为UTC时间元组
t = time.gmtime(c)
print(t)

# 将时间戳转换为本地时间元组
b = time.localtime(c)
print(b)

# 将本地时间元祖转成时间戳
m = time.mktime(b)
print(m)

# 将时间元组转换成字符串
s = time.asctime(b)
print(s)

# 将时间戳转换成字符串
p = time.ctime(c)
print(p)

# 将时间元组转换为字符串，第二个参数可以没有
q = time.strftime("%Y-%m-%d %H:%M:%S",b)
q2 = time.strftime("%Y-%m-%d %X",b)
print(q)
print(q2)

# 延迟一个时间 可以是整形或者浮点型
# time.sleep(0.3)

# 返回当前程序的CPU时间
y1 = time.clock()
print(y1)

y2 = time.clock()
print(y2)



