import pygame

pygame.init()

# 创建游戏窗口
resolution = (480,700)  # 宽高
screen = pygame.display.set_mode(resolution)

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load('./images/background.png');

# 2.绘制图像数据
screen.blit(bg,(0,0))

# 3.update更新屏幕显示
#pygame.display.update()

#绘制英雄的飞机
hero = pygame.image.load('./images/me1.png')
screen.blit(hero,(200,500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

#指定飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)

while True:
	# 可以指定循环体代码执行频率
	clock.tick(60)

	# 捕获事件
	event_list = pygame.event.get()
	for event in event_list:

		# 判断事件类型是否是退出事件
		if event.type == pygame.QUIT:
			print('退出游戏。。。')

			# 卸载所有模块
			pygame.quit()

			# 终止当前程序
			exit()
			

	# 修改飞机位置
	hero_rect.y -= 1
	# 判断飞机位置
	if hero_rect.y <= 0:
		hero_rect.y = 700

	# 调用blit方法绘制图像
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)

	pygame.display.update()


pygame.quit()