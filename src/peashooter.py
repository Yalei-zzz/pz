import objectbase
import sunlight
import time

class PeaShooter(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(PeaShooter, self).__init__(id, pos)
        self.hasShoot = False  # self.hasShoot用来判断喷出豌豆的CD
        self.hasBullet = False  # self.hasBullet用来判断是否到喷出豌豆的图片

    def hasSummon(self):
        return self.hasBullet
    
    def preSummon(self):
        self.hasShoot = True
        self.pathIndex = 0

    def doSummon(self):
        if self.hasSummon():
            self.hasBullet = False
            return sunlight.SunLight(0, (self.pos[0]+50, self.pos[1]+35))
        
    # 因为豌豆射手喷出的动画问题，不能是简单的让召唤物出现在植物旁边
    # 所以需要在peashooter这个类中重写checkImageIndex()这个方法
    def checkImageIndex(self):   # 判断延时，时间一到就返回True，可以切换图片

        # 加入一个时间间隔，防止图片切换过快
        if time.time() - self.preIndexTime < self.getImageIndexCD():
            return
        self.preIndexTime = time.time()
        idx = self.pathIndex +1
        if idx == 8 and self.hasShoot:
            self.hasBullet = True
        if idx >= self.pathIndexCount:
            idx = 9
        self.updateIndex(idx)