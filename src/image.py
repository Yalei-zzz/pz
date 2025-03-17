import pygame

class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt, pathIndex, pos, size = None, pathIndexCount=0):
        self.pathFmt = pathFmt  #
        self.pathIndex = pathIndex
        self.size = size  # 图片大小
        self.pathIndexCount = pathIndexCount
        self.pos = list(pos)  # 图片在窗口中的位置
        self.updateImage()

    def updateImage(self):
        path = self.pathFmt
        if self.pathIndexCount != 0:
            path = path % self.pathIndex
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def updateIndex(self, pathIndex):
        self.pathIndex = pathIndex
        self.updateImage()

    def updateSize(self, size):
        self.size = size
        self.updateImage()

    # 获取图片的位置，返回一个矩形
    def getRect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect

    # 实现左移
    def doLeft(self):
        self.pos[0] -= 0.1

    # 绘制图片
    def draw(self, ds):
        ds.blit(self.image, self.getRect())  # 通过getRect方法获取图片的位置，然后绘制图片