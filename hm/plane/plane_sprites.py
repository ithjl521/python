import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)

# 刷新的帧率
FRAME_PRE_SEC = 60

# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSpirte(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		#调用父类初始化方法
		super().__init__()

		#定义对象属性
		# 加载图片
		self.image = pygame.image.load(image_name)

		# 获取图片位置
		self.rect = self.image.get_rect()

		# 设置移动速度
		self.speed = speed



	def update(self):
		#在屏幕的垂直方向上移动
		self.rect.y += self.speed


class Background(GameSpirte):
	"""游戏背景精灵"""
	def __init__(self,is_alt=False):
		# 调用父类方法的精灵创建
		super().__init__('./images/background.png')
		# 判断是否有图像交替，如果是，则设置初始位置
		if is_alt:
			self.rect.y = -self.rect.height


	def update(self):
		# 调用父类方法
		super().update()

		# 判断是否移除屏幕，如果移除则将图像设置到屏幕上方
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height


class Enemy(GameSpirte):
	"""敌机精灵"""
	def __init__(self):
		super().__init__('./images/enemy1.png')

		#指定敌机初始随机速度
		self.speed = random.randint(1,3)
		# 指定敌机出事随机诶盒子
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)


	def update(self):
		super().update()

		# 判断是否飞出屏幕，如果是，从精灵组删除该精灵
		if self.rect.y >= SCREEN_RECT.height:

			# print('飞出屏幕')
			# kill方法可以将精灵从精灵组移除，精灵被自动销毁
			self.kill()


	def __del__(self):
		# print('敌机挂了%s'%self.rect)
		pass


class Hero(GameSpirte):
	"""英雄精灵"""
	def __init__(self):
		# 英雄飞机加载，并且速度为0不能移动
		super().__init__('./images/me1.png',0)

		# 指定英雄初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

		# 创建子弹精灵组
		self.bullets = pygame.sprite.Group()


	def update(self):
		# 重新update，让英雄水平移动
		self.rect.x += self.speed
		# 控制英雄不能离开屏幕
		if self.rect.x < 0 :
			self.rect.x = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		print('发射子弹')

		# 循环发射三枚子弹
		for i in (0,1,2):
			# 创建子弹精灵
			bullet = Bullet()

			# 设置精灵位置
			bullet.rect.bottom = self.rect.y - i * 20
			bullet.rect.centerx = self.rect.centerx

			# 添加到精灵组
			self.bullets.add(bullet)


class Bullet(GameSpirte):
	"""子弹精灵"""
	def __init__(self):
		# 调用父类方法，设置子弹图片和出事速度
		super().__init__('./images/bullet1.png',-2)

	def update(self):
		# 调用父类方法，让子弹垂直方向飞行
		super().update()
		# 判断子弹是否飞出屏幕
		if self.rect.bottom < 0:
			self.kill()

	def __del__(self):
		print('子弹销毁')




