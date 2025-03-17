import pygame
import image
from const import *
import sunflower


class Game(object):
    def __init__(self, ds):
        self.ds = ds
        self.back = image.Image(PATH_BACK, 0, (0, 0), GAME_SIZE, 0)
        self.plants = []
        self.summons = []
        self.hasPlant = []
        for i in range(GRID_SIZE[0]):
            col = []
            for j in range(GRID_SIZE[1]):
                col.append(0)
            self.hasPlant.append(col)

    def draw(self):
        self.back.draw(self.ds)
        for plant in self.plants:
            plant.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)

    def update(self):
        self.back.update()
        for plant in self.plants:
            plant.update()
            if plant.hasSummon():
                summ = plant.doSummon()
                self.summons.append(summ)
        for summon in self.summons:
            summon.update()

    def getIndexByPos(self, pos):  # 根据位置获取当前所处的方格位置，并返回
        x = (pos[0]-LEFT_TOP[0]) // GRID_SIZE[0]  
        y = (pos[1]-LEFT_TOP[1]) // GRID_SIZE[1]
        return x,y 

    def addSunFlower(self, x, y):
        if self.hasPlant[x][y] == 1:
            return
        self.hasPlant[x][y]=1
        pos = LEFT_TOP[0] + x*GRID_SIZE[0], LEFT_TOP[1] + y*GRID_SIZE[1]
        self.plants.append(sunflower.SunFlower(3, pos))

    def checkLoot(self, mousePos):
        pass

    def checkAddPlant(self, mousepos, objID):  # 检测并重植物，需传入位置和植物ID
        x, y = self.getIndexByPos(mousepos)
        if x < 0 or x >= GRID_COUNT[0]:
            return 
        if y <0 or y >=GRID_COUNT[1]:
            return
        if objID ==SUNFLOWER_ID:  # 如果ID为向日葵的
            self.addSunFlower(x, y)  # 通过getIndexByPos()函数获取方格位置并种下

    def mouseClickHandler(self, btn):  #  鼠标事件检测
        mousepos = pygame.mouse.get_pos()  #  获取鼠标点击的位置
        self.checkLoot(mousepos)
        if btn==1:  # 如果btn=1，说明左键按下，种下植物
            self.checkAddPlant(mousepos, SUNFLOWER_ID)  # 传入位置和要中的植物ID