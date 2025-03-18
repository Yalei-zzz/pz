
# 解决引入上一层文件夹中文件时的ImportError的问题
import os
import sys
current_path = os.path.abspath(__file__)  # 得到当前文件的绝对路径
top_path = '\\'.join( current_path.split('\\')[:-2] )  # 分割再拼接得到当前文件的根目录
sys.path.append(top_path)  # 将根目录加到系统路径里

from share.const import *

# 通过在服务端定义一个game，来接过原来在客户端实现的判断逻辑,最终返回一条给客户端的msg
class Game(object):
    def __init__(self):
        self.hasPlant = [[0]*GRID_COUNT[1] for _ in range(GRID_COUNT[0])]  # 创建哈希表

    # 原来在客户端game中的checkAddPlant中的判断逻辑在服务端实现
    # 然后改变客户端的checkAddPlant为addPlant
    def checkAddPlant(self, pos):
        msg = {
            'type' : S2C_ADD_SUNFLOWER,
            'code' : S2C_CODE_FAILED,
            'pos' : pos,
        }
        x, y = pos

        # 判断位置是否超出方格
        if x < 0 or x >= GRID_COUNT[0]:
            return msg
        if y <0 or y >=GRID_COUNT[1]:
            return msg
        
        # 判断当前位置是否有植物，不等于0，表示有植物，直接return
        if self.hasPlant[x][y] == 1:
            return msg
        
        # 如果前面的内容都未被return，即可以种植，将哈希表的该位置置为1
        # 并将要返回出去给客户端的msg中的code置为S2C_CODE_SUCCED
        self.hasPlant[x][y] = 1
        msg['code'] = S2C_CODE_SUCCED
        print( msg )
        return msg