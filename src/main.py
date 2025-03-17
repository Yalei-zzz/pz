import pygame
import sys
from game import *

from const import *
pygame.init()

DS = pygame.display.set_mode( GAME_SIZE)  # 创建窗口
pygame.display.set_caption("plants vs zombies")  # 设置窗口标题

game = Game(DS)


while True:
    for event in pygame.event.get():  # 获取事件, 如按键等
        if event.type == pygame.QUIT:  # 如果是退出事件, 则退出程序
            pygame.quit()  # 关闭所有pygame模块
            sys.exit()  # 退出程序
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.mouseClickHandler(event.button)
    game.update()
    game.draw()

    pygame.display.update()