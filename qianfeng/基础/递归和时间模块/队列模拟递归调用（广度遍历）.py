import os
import collections


def getAllDirQu(path):
	queue = collections.deque()

	# 进队
	queue.append(path)

	# 队列为空结束
	while len(queue) != 0:
		# 出队
		dirPath = queue.popleft()
		# 找出所有文件
		filesList = os.listdir(dirPath)

		for fileName in filesList:
			# 获取绝对路径
			fileAbsPath = os.path.join(dirPath,fileName)

			# 判断是否是目录
			if os.path.isdir(fileAbsPath):
				# 入队
				queue.append(fileAbsPath)
			else:
				print(fileName)





path = r'D:\python\qianfeng'
getAllDirQu(path)


