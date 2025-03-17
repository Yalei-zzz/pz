import pygame
import image
from const import *
import sunflower
import data_object


class Game(object):
    def __init__(self, ds):
        self.ds = ds
        self.back = image.Image(PATH_BACK, 0, (0, 0), GAME_SIZE, 0)
        self.plants = []
        self.summons = []
        self.hasPlant = []
        self.gold = 300
        self.goldFont = pygame.font.Font(None, 60)  # None表示默认字体
        for i in range(GRID_SIZE[0]):
            col = []
            for j in range(GRID_SIZE[1]):
                col.append(0)
            self.hasPlant.append(col)

    def renderFont(self):
        textImage = self.goldFont.render("Gold: "+str(self.gold), True, (0, 0, 0))
        self.ds.blit(textImage, (13, 23))
        textImage = self.goldFont.render("Gold: "+str(self.gold), True, (255, 255, 255))
        self.ds.blit(textImage, (10, 20))

    def draw(self):  # 做整个游戏的绘制工作
        self.back.draw(self.ds)
        for plant in self.plants:
            plant.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)

        self.renderFont()

    def update(self):  # 做整个游戏的画面更新
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

    def addSunFlower(self, x, y):  # 种下向日葵
        self.hasPlant[x][y]=1
        pos = LEFT_TOP[0] + x*GRID_SIZE[0], LEFT_TOP[1] + y*GRID_SIZE[1]
        self.plants.append(sunflower.SunFlower(SUNFLOWER_ID, pos))
        

    # 是否捡起一个object，如果捡起了，就返回True，在此次鼠标事件之后不在执行其他的操作
    def checkLoot(self, mousePos):  
        for summon in self.summons:
            # 判断object是否可以拾取，如果不可以就直接继续循环，不需要执行其他操作
            if not summon.canLoot():  
                continue  
            # 如果可以捡，就要判断鼠标点击的位置是否为当前object的方格
            rect = summon.getRect()
            if rect.collidepoint(mousePos):
                self.summons.remove(summon)
                self.gold += summon.getPrice()
                return True
        return False


    def checkAddPlant(self, mousepos, objID):  # 检测并重植物，需传入位置和植物ID
        x, y = self.getIndexByPos(mousepos)
        if x < 0 or x >= GRID_COUNT[0]:
            return 
        if y <0 or y >=GRID_COUNT[1]:
            return
        if self.gold < data_object.data[objID]['PRICE']:  # 检测当前金币是否可以种
            return
        if self.hasPlant[x][y] == 1:
            return

        self.gold -= data_object.data[objID]['PRICE']
        if objID ==SUNFLOWER_ID:  # 如果ID为向日葵的
            self.addSunFlower(x, y)  # 通过getIndexByPos()函数获取方格位置并种下
            

    def mouseClickHandler(self, btn):  #  鼠标事件检测
        mousepos = pygame.mouse.get_pos()  #  获取鼠标点击的位置
        if self.checkLoot(mousepos):
            return
        if btn==1:  # 如果btn=1，说明左键按下，种下植物
            self.checkAddPlant(mousepos, SUNFLOWER_ID)  # 传入位置和要种的植物ID