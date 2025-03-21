
data = {
    # 子弹属性表
    0 :{ 
        "PATH" : "pz/pic/other/peabullet.png",  # 加载子弹的路径
        'IMAGE_INDEX_MAX' : 0, # 子弹自动画图片数量
        'IMAGE_INDEX_CD' : 0.3,  # 子弹图片切换的时间
        'POSITION_CD' : 0.005, # 子弹位置切换的时间间隔
        'SUMMON_CD' : -1,  # 没有召唤物，则为-1
        'SIZE' : (39, 39),  # 子弹的大小
        'SPEED' : (3, 0),  # 子弹的速度
        'CAN_LOOT' : False,  # 是否可拾取
        'PRICE' : 0,  # 子弹的金币为0
        'HP' : 1,  # 血量
        'ATT' : 1,  # 攻击值
    },
    # 僵尸一号属性表
    1 :{
        "PATH" : "pz/pic/zombie/0/%d.png",
        'IMAGE_INDEX_MAX' : 15,
        'IMAGE_INDEX_CD' : 0.3,
        'POSITION_CD' : 0.08,
        'SUMMON_CD' : -1,
        'SIZE' : (100, 128),
        'SPEED' : (-0.6, 0),
        'CAN_LOOT' : False,  # 是否可拾取
        'PRICE' : 0,  # 僵尸价值金币为0
        'HP' : 5,  # 血量
        'ATT' : 1,  # 攻击值
    },
    # 阳光属性表
    2 :{
        "PATH" : "pz/pic/other/sunlight/%d.png",
        'IMAGE_INDEX_MAX' : 30,
        'IMAGE_INDEX_CD' : 0.08,
        'POSITION_CD' : 0.05,
        'SUMMON_CD' : -1,
        'SIZE' : (80, 80),
        'SPEED' : (0, 2),
        'CAN_LOOT' : True,  # 是否可拾取
        'PRICE' : 50,  # 阳光价值金币为50
        'HP' : 10000,  # 血量
        'ATT' : 0,  # 攻击值
    },
    # 向日葵属性表
    3 :{
        "PATH" : "pz/pic/plant/sunflower/%d.png",
        'IMAGE_INDEX_MAX' : 19,
        'IMAGE_INDEX_CD' : 0.08,
        'POSITION_CD' : -1,
        'SUMMON_CD' : 10,  # 定义多久召唤一次阳光
        'SIZE' : (128, 128),
        'SPEED' : (0, 0),
        'CAN_LOOT' : False,  # 是否可拾取
        'PRICE' : 100,  # 向日葵价值金币为100
        'HP' : 5,  # 血量
        'ATT' : 0,  # 攻击值
    },
    # 豌豆射手属性表
    4 :{
        "PATH" : "pz/pic/plant/peashooter/%d.png",
        'IMAGE_INDEX_MAX' : 19,
        'IMAGE_INDEX_CD' : 0.1,
        'POSITION_CD' : -1,
        'SUMMON_CD' : 3,  # 定义多久发射一颗子弹
        'SIZE' : (128, 128),
        'SPEED' : (0, 0),
        'CAN_LOOT' : False,  # 是否可拾取
        'PRICE' : 100,  # 向日葵价值金币为100
        'HP' : 5,  # 血量
        'ATT' : 0,  # 攻击值
    },

}