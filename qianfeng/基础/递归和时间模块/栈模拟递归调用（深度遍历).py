
import os


def getAllDirDe(path):
	
	stack = []
	stack.append(path)

	# 一直到空栈为止
	while len(stack) != 0:
		dirPath = stack.pop()

		# 获取当前路径的所有目录
		filesList = os.listdir(dirPath)

		# 遍历当前路径的所有文件
		for fileName in filesList:
			fileAbsPath = os.path.join(dirPath,fileName)

			# 判断路径是否是目录
			if os.path.isdir(fileAbsPath):
				# 压栈
				stack.append(fileAbsPath)
			else:
				# 打印普通文件
				print(fileName)


path = r'D:\python\qianfeng'
getAllDirDe(path)



