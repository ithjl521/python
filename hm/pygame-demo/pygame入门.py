import pygame


rect = pygame.Rect(100,500,120,125)
print('横坐标%d-纵坐标%d'%(rect.x,rect.y))
print('宽%d-高%d'%(rect.width,rect.height))
print(rect.size)

pygame.init()

# 编写游戏代码



pygame.quit()