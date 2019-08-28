import os
# print(os.name)  #获取操作系统类型，nt->window posix->unix/mac os x

#打印操作系统详细信息 linux系统1
#print(os.uname())

# 获取操作系统环境变量
# print(os.environ)

# 获取指定环境变量
# print(os.environ.get('APPDATA'))

# 获取当前目录
# print(os.curdir)

# 获取当前工作目录
# print(os.getcwd())

# 返回指定目录下所有文件，以列表形式
# print(os.listdir('.'))

# 在当前目录下创建新目录
# os.mkdir('hjl')

# 删除当前目录下的指定目录
# os.rmdir('./hjl')

# 获取文件属性
# print(os.stat('os模.py'))

# 文件重命名
# os.rename('test.txt','test1.py')

# 删除文件
# os.remove('test1.py')

# 运行shell命令
# os.system('notepad')
# os.system('taskkill /f /im notepad.exe')
# os.system('write')
# os.system('mspaint')



# 查看当前绝对路径
# print(os.path.abspath('.'))

# 拼接路径 参数2开始不要有斜杠
# p1 = 'D:/python/'
# p2 = 'qianfeng/demo.py'
# print(os.path.join(p1,p2))

# 拆分路径 
# path = 'D:/python/qianfeng/demo.py'
# print(os.path.split(path))

# 获取扩扎名
# path = 'D:/python/qianfeng/demo.py'
# print(os.path.splitext(path))


# 获取文件所在目录
# print(os.path.dirname('test.txt'))


# 判断是否是目录
# print(os.path.isdir('d:/python'))

# 判断文件是否存在
# print(os.path.isfile('test.txt'))

# 判断目录是否存在
# print(os.path.exists('d:/python'))

# 获取文件大小 字节
# print(os.path.getsize('./test.txt'))


