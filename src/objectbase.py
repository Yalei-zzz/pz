import image
import time
import data_object

class ObjectBase(image.Image):
    def __init__(self, id, pos):
        self.id = id
        self.preIndexTime = 0
        self.prePositnIime = 0
        self.preSummonTime = 0
        super(ObjectBase, self).__init__(
            self.getID()['PATH'], 
            0, 
            pos, 
            self.getID()['SIZE'], 
            self.getID()['IMAGE_INDEX_MAX'])

    def update(self):
        self.checkImageIndex()  
        self.checkPosition()  
        self.checkSummon()

    def getPositionCD(self):  # 直接从表中获取切换位置的时间间隔
        return self.getID()['POSITION_CD']

    def getImageIndexCD(self):  # 直接从表中获取切换图片的时间间隔
        return self.getID()['IMAGE_INDEX_CD']
    
    def getSpeed(self):  # 直接从表中获取速度
        return self.getID()['SPEED']
    
    def getSummonCD(self):  # 从表中获取多久召唤一次召唤物
        return self.getID()['SUMMON_CD']

    def checkImageIndex(self):   # 判断延时，时间一到就返回True，可以切换图片

        # 加入一个时间间隔，防止图片切换过快
        if time.time() - self.preIndexTime < self.getImageIndexCD():
            return
        self.preIndexTime = time.time()

        # 在内部设置循环，实现图片的切换
        idx = self.pathIndex +1
        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)

    def checkPosition(self):  # 判断延时，时间一到就返回True，可以移动

        """之前判断位置是否改变是通过在基类中写一个判断,如果时间到了就返回True,然后再子类中
        调用这个方法,如果子类得到了True,就会改变位置,也是因为改变位置得方向得大小不一样,所以
        在子类中实现。现在可以通过调用表中数据的方式来直接在基类中实现不同对象的移动,所以现在
        所有的对象的功能都是通过调用表中的属性在基类中实现。"""

        if time.time() - self.prePositnIime < self.getPositionCD():
            return False
        self.prePositnIime = time.time()
        speed = self.getSpeed()
        self.pos = (self.pos[0]+speed[0], self.pos[1]+speed[1])
        return True
    
    def checkSummon(self):  # 判断延时，时间一到就返回True，可以召唤
        if time.time() - self.preSummonTime < self.getSummonCD():
            return
        self.preSummonTime = time.time()
        self.preSummon()
    
    def getID(self):  # 获取想要创建对象的id
        return data_object.data[self.id]
    
    def preSummon(self):  # 预召唤,在子类中实现
        pass
        
    def hasSummon(self):
        pass

    def doSummon(self):
        pass

