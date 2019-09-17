import time
import pygame

# 音乐路径
filePath = "D:\python\python\qianfeng\其他\播放音乐\你的香气.mp3"

#初始化
pygame.mixer.init()

# 加载音乐
track = pygame.mixer.music.load(filePath)

# 播放
pygame.mixer.music.play()

# 暂停
time.sleep(10)

# pygame.mixer.music.pause() 暂停/继续

# 停止
pygame.mixer.music.stop()

