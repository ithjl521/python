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
pygame.display.update()

#绘制英雄的飞机
hero = pygame.image.load('./images/me1.png')
screen.blit(hero,(200,500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

i = 0

while True:
	# 可以指定循环体代码执行频率
	clock.tick(60)
	
	print(i)
	i += 1

pygame.quit()