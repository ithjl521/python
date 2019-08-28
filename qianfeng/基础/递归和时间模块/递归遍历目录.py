import os

def getAllDir(path):
	# 获取当前目录所有文件和目录
	filesList = os.listdir(path)
	for fileName in filesList:
		# 判断是否是路径
		absPath = os.path.join(path,fileName)
		if os.path.isdir(absPath):
			print('目录',absPath)
			getAllDir(absPath)
		else:
			print('文件',fileName)

path = r'D:\python\qianfeng'
getAllDir(path)
